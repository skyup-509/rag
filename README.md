# RAG
## 문제
- 비정형 데이터가 지속적으로 증가
- 필요한 정보를 찾기 위해 문서를 직접 확인해야 하여, 원하는 정보를 찾는 데 많은 시간과 반복 작업이 발생
- 데이터가 여러 문서와 형식으로 분산되어 있음
- 축적된 데이터를 효과적으로 활용하기 어려움

## 목적
- 비정형 데이터를 쉽게 검색하고 활용
- 정보 탐색에 드는 시간과 비용 절감
- LLM을 활용한 데이터 접근성 향상
- RAG의 전체 동작 과정을 직접 구현하고 이해

## 기대 효과
- 자연어 기반의 정보 검색
- 필요한 정보의 빠른 탐색
- 비정형 데이터 활용성 향상
- 반복적인 정보 탐색 작업 감소
- 데이터 접근성 및 생산성 향상

## 한계
- 단순한 Chunking으로 인한 정보 분리 가능성
- Vector Search만으로는 검색 품질에 한계가 존재
- 검색 결과에 따라 답변 품질이 달라질 수 있음
- 대규모 데이터 환경에 대한 고려 부족
- Retrieval 및 Generation에 대한 정량적 평가 부족

## 개선 방향
- Hybrid Search
- Reranking
- Semantic Chunking
- Metadata Filtering
- Query Transformation
- RAG Evaluation
- 답변 근거 및 출처 제공

## Timeline (In Progress)

### 2026-09-01 · [01_basic]

- reference를 참고하여 기본 RAG 구축

### 2026-09-07 · [02_basic]

- PDF $\rightarrow$ Vector DB 구축과 Chat 기능 분리
- `util/git_push.py` 구현
  - Colab 환경에서 실행 가능
  - 실행 결과 Git push 자동화