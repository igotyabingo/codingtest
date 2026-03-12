# 조삼모사

[문제 링크](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/three-at-dawn-and-four-at-dusk/description) 

### 성능 요약

메모리: 19 MB, 시간: 843 ms

### 구분

삼성 기출 문제 > 2017 하반기 오전 1번 문제

### 제출 일자

2026년 03월 11일 10:31

### 문제 설명

<p><code>n</code>개의 일이 주어질 때 이를 아침과 저녁으로 각각 <code>n/2</code>개씩 나누어 처리하고자 합니다. 일마다 특성이 다르기 때문에 같이할 때의 업무 강도를 나타내는 업무 간의 상성 <code>P<sub>ij</sub></code>가 존재합니다. 예를 들어 업무 상성이 다음과 같이 주어질 때,</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/e7385a4e-2e09-4f17-96ea-f4d63add2b42" width="200"/>
</p>

<p>1, 2번 일을 아침에, 3, 4번 일을 저녁에 한다면 아침의 총 업무 강도는 <code>P<sub>12</sub> + P<sub>21</sub> = 8</code>이 되고, 저녁의 총 업무 강도는 <code>P<sub>34</sub> + P<sub>43</sub> = 13</code>이 됩니다.</p>
<p>만약 1, 4번 일을 아침에, 2, 3번 일을 저녁에 한다면 아침의 경우 <code>P<sub>14</sub> + P<sub>41</sub> = 2</code>, 저녁의 경우 <code>P<sub>23</sub> + P<sub>32</sub> = 9</code>가 됩니다. 아침과 저녁의 일의 힘든 정도가 너무 차이가 나면 일하기가 싫어지기 때문에, 아침의 하는 일의 업무 강도와 저녁에 하는 일의 업무 강도의 차이의 최솟값을 구하고자 합니다. 위의 예시의 경우 1,2번 일과 3,4번의 일로 나누어서 하는 것이 힘듦의 합의 차이가 5로 최솟값이 됩니다.</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/69ec45ea-7bb1-4821-b9e6-d96cce3a13f8" width="200"/>
</p>

<p>6개의 일이 주어질 때 아침에 2,3,4번일, 저녁에 1,5,6 번 일을 한다고 했을 때, 아침의 경우 <code>P<sub>23</sub> + P<sub>32</sub> + P<sub>34</sub> + P<sub>43</sub> + P<sub>24</sub> + P<sub>42</sub> = 64</code>, 저녁의 경우 <code>P<sub>15</sub> + P<sub>51</sub> + P<sub>56</sub> + P<sub>65</sub> + P<sub>16</sub> + P<sub>61</sub> = 45</code>가 됩니다.</p>

<p>아침과 저녁의 업무 강도의 차이의 최솟값을 구하는 프로그램을 작성하세요.</p>