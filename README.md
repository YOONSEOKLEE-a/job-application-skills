# Job Application Skills

한국 채용 지원서 작성과 자소서 작성을 위한 Codex 스킬 공유본입니다. 특정 지원자의 개인정보 없이, 각 사용자의 자료를 읽어 동작하도록 정리했습니다.

| 스킬 | 기능 |
|---|---|
| [apply](skills/apply/SKILL.md) | 채용 사이트 로그인, 원본 프로필 기반 입력, 전체 이력 누락 점검, 저장·승인된 제출 확인 |
| [tailored-jasoseo](skills/tailored-jasoseo/SKILL.md) | 경험 근거 정리, 기업·직무별 사례 선택, 자소서 작성·검토·Markdown 보관·DOCX 내보내기 |

## 설치

이 저장소를 내려받아 필요한 스킬 폴더를 자신의 Codex 개인 스킬 폴더에 복사하세요. 기존 동명 스킬이 있으면 먼저 백업하고 내용을 비교하세요.

```text
skills/apply/             → ~/.codex/skills/apply/
skills/tailored-jasoseo/   → ~/.codex/skills/tailored-jasoseo/
```

Windows의 `~`는 본인 사용자 홈 폴더입니다. `CODEX_HOME`을 별도로 설정했다면 그 아래 `skills/`를 사용하세요. 설치 뒤 새 대화에서 `$apply` 또는 `$tailored-jasoseo`를 호출하세요.

## 사용 예시

```text
$apply 크롬에 열린 채용 공고와 내 자료 폴더를 확인하고 지원서를 작성해줘. 최종제출 전까지만 진행해.

$tailored-jasoseo 내 이력서와 경험 정리를 바탕으로 이 회사의 실제 자소서 문항에 맞는 답변을 작성해줘.
```

각 사용자가 자신의 프로필·경험·증빙·지원 문항과 자료 위치를 제공해야 합니다. 경험 우선순위와 사실은 해당 사용자의 자료에서 확인합니다. 지원서 제출은 그 사용자가 허용한 범위에서만 진행합니다.

## 개인 자료 보관

- 이름, 연락처, 학력·성적, 개인 경력·연구 이력, 실제 자소서, 피드백, 지원 결과, 로그인 정보, 개인 경로·대화 ID는 포함하지 않았습니다.
- 원본 스킬의 비공개 Git 이력과 문서·예시 캐시, 자격증명 조회 스크립트는 포함하지 않았습니다.
- `tailored-jasoseo/assets/templates/`는 내용이 비어 있는 양식입니다. 개인 Obsidian vault나 저장소 밖의 자료 폴더에 복사한 뒤 작성하세요. 공개 저장소 안의 양식 자체에 개인정보를 쓰지 마세요.
- `private-data/`와 `outputs/`는 Git 제외 대상으로 설정했습니다. `.gitignore`가 모든 개인정보를 자동으로 탐지하는 것은 아니므로 새 파일을 올릴 때 내용을 확인하세요.

## 도구와 선택 기능

`apply`는 현재 환경에서 제공하는 브라우저 제어 도구가 필요합니다. 이 패키지는 브라우저 플러그인, 계정, 로그인 세션을 설치하거나 제공하지 않습니다.

`tailored-jasoseo`는 Markdown과 로컬 자료만으로도 사용할 수 있습니다. Obsidian, NotebookLM, `humanize-korean`은 선택 연동이며 포함되어 있지 않습니다. 개인 자료를 외부 서비스로 올릴 때는 해당 사용자의 허용 범위를 따릅니다. 실제 예시 자소서 모음과 연구·예시 동기화 스크립트는 공유본에 포함하지 않아 해당 단계는 수동 대체합니다.

글자 수 확인은 Python 표준 라이브러리만 사용합니다.

```bash
python skills/tailored-jasoseo/scripts/count_jasoseo_sections.py draft.md
```

인식하는 Markdown 문항 제목 형식은 `## 1. 지원동기 (700자 이내)`입니다. 공백·줄바꿈을 포함한 Python 문자열 길이를 계산하며, 사이트의 byte 계산이나 별도 집계 규칙은 사이트에서 확인해야 합니다. 기본 최소 사용률은 90%이며 `--min-ratio`로 조정할 수 있습니다.

DOCX 내보내기는 `python-docx`가 필요합니다.

```bash
python -m pip install python-docx
python skills/tailored-jasoseo/scripts/export_jasoseo_docx.py final_answers.json --output outputs/jasoseo.docx
```

JSON 입력 형식은 [스킬의 DOCX 내보내기 절](skills/tailored-jasoseo/SKILL.md)에 있습니다. `--output`을 생략하면 현재 작업 폴더의 `outputs/`에 저장합니다. 스크립트는 파일을 생성하며 최종 인쇄 레이아웃 검토는 별도입니다.
