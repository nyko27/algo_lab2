# algo_lab2
���������� ��������� �������� ������i�. �� ����i ������i i�����, �����, ��
���������, ���� ����� �i���� ������� �����i���.
��� ����, ��� ����������� �������, ���� ���� �������i, ����i��� H �����i� �����
�� ����. �����, ���� �i���� ������i� ������ �����, � ��� ����������� ���i��i���.
� ������ ������� ����� ������� 璿�� ��������� G �����i� ����� � ���� ��
������� ���i��. ����� ����� H �� ���i��i��� G � i����i��������� ��� �������
�������.
������ � �������i � C ������i�. �� ������ �������� ������� �i����, ����� � ���
� ������ S �����i� ��i �� ����. �������� ����������� �i���i��� ������i�, ��� ��
������ �����������.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Time complexity of the alorithm is O(n^2), because max_count_if_few_hamsters() function recursively calls itself with list in parmeter which has 1 less element
then previous call of this function and this function has for loop which iterates through input list.
In case when input list has 3 elements(only 1 hamster), comlexity is O(1).

max_count_if_few_hamsters() function calculates total hunger of all hamsters and if the value of this hunger is bigger then S(nuber of all packages for this day),
removes hamster which has the biggest hunger. Then function recursively calls itself, but with new input list until total hunger of all hamsters is smaller then S.

max_hamsters_count_with_edge_case() function returns result of max_count_if_few_hamsters() function if it isn't 0. If max_count_if_few_hamsters() function returns 0,
max_hamsters_count_with_edge_case() checks case when there is only 1 hamster who can be fed (using simple for loop and primary input). If it so, function returns 1, 
else it returns 0. Also if the size of input list is 3, there's "if else" statement which reduces algorithm complexity to O(1).


------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If you want to run this project without using ide, use "python main.py -v" command in your terminal