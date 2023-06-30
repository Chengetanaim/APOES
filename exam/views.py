from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import threading
import winsound
from datetime import datetime
from datetime import date
import cv2
import imutils
from .models import Alert, Exam, ExamQuestion, Answer, StructuredQuestion, ExamDuration, Disqualified
from django.http import HttpResponse


def index(request):
    mutiple_choice_exam = Exam.objects.filter(exam_type="Multiple Choice")
    structured_exam = Exam.objects.filter(exam_type="Structured")
    context = {'multiple_choice_exam': mutiple_choice_exam, 'structured_exam': structured_exam}
    return render(request, 'exam/index.html', context)


@login_required()
def multiple_choice(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam_questions = ExamQuestion.objects.filter(exam=exam)
    answers = Answer.objects.filter(exam=exam)
    endtime = exam.endtime
    start_time = exam.endtime
    context = {'exam': exam, 'exam_questions': exam_questions, 'answers': answers, 'endtime': endtime, 'start_time': start_time}
    return render(request, 'exam/multiple_choice.html', context)


@login_required()
def structured(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam_questions = StructuredQuestion.objects.filter(exam=exam)
    context = {'exam': exam, 'exam_questions': exam_questions}
    return render(request, 'exam/structured.html', context)


@login_required()
def proctor(request):
    user = request.user
    ExamDuration.objects.create(user=user)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    _, start_frame = cap.read()
    start_frame = imutils.resize(start_frame, width=500)
    # Removing any colours
    start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)

    # Smoothening the video
    start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

    alarm = False
    # Press t to toggle alarm
    alarm_mode = True
    # Amount of movement to turn on alarm
    alarm_counter = 0

    def beep_alarm():
        global alarm
        for _ in range(5):
            if not alarm_mode:
                break
            print("alarm")
            winsound.Beep(2500, 1000)
        alarm = False

    while True:
        _, frame = cap.read()
        frame = imutils.resize(frame, width=500)

        if alarm_mode:
            frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)
            difference = cv2.absdiff(frame_bw, start_frame)
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
            start_frame = frame_bw

            if threshold.sum() > 300:
                alarm_counter += 1
            else:
                if alarm_counter > 0:
                    alarm_counter -= 1

            cv2.imshow("Cam", threshold)
        else:
            cv2.imshow("Cam", frame)

        if alarm_counter > 50:
            if not alarm:
                alarm = True
                threading.Thread(target=beep_alarm).start()
                Alert.objects.create(user=user)



        key_pressed = cv2.waitKey(30)
        if key_pressed == ord("t"):
            alarm_mode = not alarm_mode
            alarm_counter = 0
        if key_pressed == ord("q"):
            alarm_mode = False
            break

    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'exam/proctor.html')


def alert(request):
    alerts = Alert.objects.all()
    context = {'alerts': alerts}
    return render(request, 'exam/alert.html', context)


def disqualified(request):
    user = request.user
    Disqualified.objects.create(user=user)
    success = user, ", you have been disqualified!"
    return HttpResponse(success)



