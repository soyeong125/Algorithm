# DP
T = int(input())
for t in range(T):
    fee = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    result = [0]*13  #����� ���� 
    for i in range(1,13):
        a = [0,0,987654321,987654321] #�̹��� ��� ��� ���� , �� ���߿��� ���� �ּ� ���� �״��� �ּҰ�
        a[0] = result[i-1] + fee[0]*plan[i-1] #1�ϱ� ����ϴ� ���: ������ ��� + ���ϱ�
        a[1] = result[i-1] + fee[1] # 1�� ����ϴ� ��� : ������ ��� + �Ѵޱ�
        if i >= 3: #3�� �̻��� ���, ex) 0�� + (1,2,3��) 3����ġ ��� 
            a[2] = result[i-3] + fee[2]
        if i == 12: # 12���� ��� 1��ġ ��� ����ؼ� �������� �����ݾ׵�� �ּұݾ� ��
            a[3] = fee[3]
        result[i] = min(a) #1��, 1��, 3�� , 1��ġ �� �ּҰ� ����
    print('#{} {}'.format(t,result[12]))
    