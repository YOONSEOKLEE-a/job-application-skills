#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt


DEFAULT_OUTPUT_DIR = Path.cwd() / "outputs"
BODY_FONT = "Malgun Gothic"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9가-힣._-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "jasoseo"


def read_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def set_style_font(style, size: int, bold: bool | None = None) -> None:
    style.font.name = BODY_FONT
    style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    style._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)


def build_document() -> Document:
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Pt(56)
    section.bottom_margin = Pt(56)
    section.left_margin = Pt(64)
    section.right_margin = Pt(64)

    set_style_font(doc.styles["Normal"], 10)
    set_style_font(doc.styles["Title"], 16, bold=True)
    set_style_font(doc.styles["Heading 1"], 12, bold=True)
    set_style_font(doc.styles["Heading 2"], 11, bold=True)
    return doc


def normalize_sections(payload: dict) -> list[dict]:
    if isinstance(payload.get("questions"), list):
        return payload["questions"]
    if isinstance(payload.get("sections"), list):
        return payload["sections"]
    if payload.get("body"):
        return [
            {
                "question_label": payload.get("question_label", "자기소개서"),
                "question": payload.get("question", ""),
                "answer": payload["body"],
                "character_limit": payload.get("character_limit"),
            }
        ]
    raise ValueError("Payload must contain `questions`, `sections`, or `body`.")


def add_title_block(doc: Document, payload: dict) -> None:
    title = payload.get("title") or "Tailored Jasoseo"
    paragraph = doc.add_paragraph(style="Title")
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(title)
    run.font.name = BODY_FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)

    meta_parts = []
    for key in ("company", "role", "team"):
        value = payload.get(key)
        if value:
            meta_parts.append(value)
    if meta_parts:
        meta = doc.add_paragraph()
        meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
        meta_run = meta.add_run(" | ".join(meta_parts))
        meta_run.font.name = BODY_FONT
        meta_run.font.size = Pt(10)
        meta_run._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)


def add_answer_section(doc: Document, index: int, section: dict) -> None:
    label = section.get("question_label") or f"{index}번 문항"
    doc.add_paragraph(label, style="Heading 1")

    question = (section.get("question") or "").strip()
    if question:
        prompt_paragraph = doc.add_paragraph(style="Heading 2")
        prompt_run = prompt_paragraph.add_run(question)
        prompt_run.font.name = BODY_FONT
        prompt_run._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)

    character_limit = section.get("character_limit")
    if character_limit:
        limit_paragraph = doc.add_paragraph()
        limit_run = limit_paragraph.add_run(f"글자 수 기준: {character_limit}")
        limit_run.italic = True
        limit_run.font.name = BODY_FONT
        limit_run.font.size = Pt(9)
        limit_run._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)

    answer = (section.get("answer") or "").replace("\r\n", "\n").strip()
    paragraphs = [block.strip() for block in re.split(r"\n\s*\n", answer) if block.strip()]
    for block in paragraphs:
        paragraph = doc.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(8)
        run = paragraph.add_run(block)
        run.font.name = BODY_FONT
        run.font.size = Pt(10)
        run._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)


def derive_output_path(payload: dict, requested_output: str | None) -> Path:
    if requested_output:
        path = Path(requested_output)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path

    company = payload.get("company", "company")
    role = payload.get("role", "role")
    title = payload.get("title", "jasoseo")
    filename = f"{slugify(company)}-{slugify(role)}-{slugify(title)}.docx"
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return DEFAULT_OUTPUT_DIR / filename


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a tailored jasoseo payload to DOCX.")
    parser.add_argument("input_json", help="Path to a JSON payload describing the final answers.")
    parser.add_argument("--output", help="Explicit output DOCX path.")
    args = parser.parse_args()

    input_path = Path(args.input_json)
    payload = read_payload(input_path)
    sections = normalize_sections(payload)

    doc = build_document()
    add_title_block(doc, payload)
    doc.add_paragraph("")
    for index, section in enumerate(sections, start=1):
        add_answer_section(doc, index, section)

    output_path = derive_output_path(payload, args.output)
    doc.save(str(output_path))
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
