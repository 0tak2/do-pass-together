'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/92334
- 유형: 구현
'''

def solution(id_list, report, k):
    answer = []
    report_board = {}
    total_report = {}
    account_suspension = []
    report = set(report)
    
    # 신고 현황 저장 (신고자: [피신고자])
    for i in report:
        x, y = i.split(' ')
    
        if x in report_board.keys():
            report_board[x].append(y)
        else:
            report_board[x] = [y]

    # 누적 신고 횟수 
    for key, value in report_board.items():
        for v in value:
            if v in total_report.keys():
                total_report[v] += 1
            else:
                total_report[v] = 1
                
    # 정지 유저 리스트
    for idx, val in total_report.items():
        if val >= k:
            account_suspension.append(idx)
    
    # 정지 횟수 카운팅
    for user in id_list:
        temp = 0
        if user in report_board.keys():
            for stop in account_suspension:
                if stop in report_board[user]:
                    temp += 1
                    
        answer.append(temp)
    
    return answer