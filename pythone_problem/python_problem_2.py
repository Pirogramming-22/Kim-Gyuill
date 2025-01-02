#함수 이름은 변경 가능합니다.

# 학생 딕셔너리
students = {}

# menu 1: 학생 정보 저장
def insert_student_info(name, mid, final) :
    students[name] = {'mid' : mid, 'final' : final, 'grade' : None}
    

# menu 2: 학점 부여
def grading() :
    
    # 학점이 부여돼있으면 스킵
    for name, scores in students.items():
        if scores['grade'] is not None:
            continue
        
        avg = (scores['mid'] + scores['final']) / 2
        
        if avg >= 90:
            scores['grade'] = 'A'
        elif avg >= 80:
            scores['grade'] = 'B'
        elif avg >= 70:
            scores['grade'] = 'C'
        else:
            scores['grade'] = 'D'
                
# menu 3: 학생 정보 출력
def printing_info() :
    #출력 코딩
    print("Name Mid Final Grade")
    print("-" * 30)
    for name, info in students.items():
        print(f"{name} {info['mid']} {info['final']} {info['grade']}")

# ##############  menu 4
# def Menu4(#매개변수가 필요한지 판단 후 코딩할 것):
#     #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    
    # 학생 정보 입력
    if choice == "1":
        try:
            #학생 정보 입력받기
            student_info = input("Enter name mid-score final-score : ").split()
            
            # 예외 처리 - 데이터 입력 갯수
            if len(student_info != 3):
                print("Num of data is not 3!")
                continue
                
            # 예외처리 - 이름 중복
            name, mid_score, final_score = student_info
            if name in students:
                print("Already exist name!")
                continue
            
            # 예외처리 - 점수 범위
            if not mid_score.isdigit() or not final_score.isdigit():
                print("Score is not positive integer!")
                continue
            
            # 1번 메뉴 호출
            insert_student_info(name, int(mid_score), int(final_score))
            
        # 그 외 예외처리
        except Exception as e:
            print(e)

    # 학점 부여
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if not students:
            print("No student data!")
            continue
        #예외사항이 아닌 경우 2번 함수 호출
        else:
            grading()
        #"Grading to all students." 출력
        print("Grading to all students.")

    # 학생 정보 출력
    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if not students:
            print("No student data!")
            continue
        
        for name, info in students.items():
            if info['grade'] is None:
                print(f"There is a student who didn't get grade.")
                continue
            
        #예외사항이 아닌 경우 3번 함수 호출
        printing_info();

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number. Choose again.")
        continue