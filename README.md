# 알라딘 중고매장 책 정보 검색하기

> 매번 알라딘 중고매장에서 책 있는지 확인하기 위해서 뒤지는 시간들을 아끼기 위해서 만들었다.

## Usage
```bash
# Install

bash> git clone https://github.com/TaeHyoungKwon/aladin_reuse_book_store_search.git
bash> cd aladin_reuse_book_store_search
bash> pip install requirements.txt
```

```bash
# Search Book

bash> python crawling_aladin.py [책 제목]

ex)
bash> python crawling_aladin.py "파이썬"
bash> python crawling_aladin.py "python"
```

```bash
# Success

bash> python crawling_aladin.py "파이썬"


이 결과는 알라딘 중고매장에서 검색된 결과 입니다.

검색된 책은 총 25 권 입니다.

1. 두근두근 파이썬
2. 파이썬 코딩 도장
3. 모두의 데이터 분석 with 파이썬
4. 모두의 알고리즘 with 파이썬
5. 파이썬으로 데이터 주무르기
6. 파이썬 라이브러리를 활용한 머신러닝
7. 파이썬 웹 프로그래밍
8. 처음 시작하는 파이썬
9. 파이썬 날코딩으로 알고 짜는 딥러닝
10. 파이썬으로 웹 크롤러 만들기
11. 윤성우의 열혈 파이썬 : 중급편
12. 데이터 분석을 위한 파이썬 철저 입문
13. 마인크래프트로 배우는 파이썬 프로그래밍
14. 바이오파이썬으로 만나는 생물정보학
15. 파이썬을 활용한 금융공학 레시피
16. 밑바닥부터 시작하는 딥러닝
17. 깔끔한 파이썬 탄탄한 백엔드
18. 뇌를 자극하는 파이썬 3
19. 파이썬 정복
20. 처음 만나는 파이썬
21. 파이썬에 참 좋은 PyCharm
22. 코딩 클럽 LV1 : 모두를 위한 파이썬 기초
23. 빠르게 활용하는 파이썬 3.6 프로그래밍
24. 누구나 쉽게 배우는 파이썬 프로그래밍
25. 프로그래머를 위한 베이지안 with 파이썬

```

```bash
# Not Found

bash> python crawling_aladin.py "대규모 서비스를 지탱하는 기술"


찾으려는 책이 없습니다.
```