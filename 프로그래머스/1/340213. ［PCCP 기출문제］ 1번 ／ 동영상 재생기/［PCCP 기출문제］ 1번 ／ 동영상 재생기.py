def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 영상 길이 초단위로 변환
    video_split = video_len.split(":")
    video = int(video_split[0]) * 60 + int(video_split[1])
    
    # 현재 재생 위치 초단위로 변환
    now_split = pos.split(":")
    now = int(now_split[0]) * 60 + int(now_split[1])
    
    # 오프닝 시작 시간 초단위로 변환
    start_split = op_start.split(":")
    start = int(start_split[0]) * 60 + int(start_split[1])

    # 오프닝 종료 시간 초단위로 변환
    end_split = op_end.split(":")
    end = int(end_split[0]) * 60 + int(end_split[1])

    for command in commands:
        if now >= start and now <= end:
            now = end
        if command == "prev":
            prev_time = now - 10
            if prev_time >= start and prev_time <= end:
                now = end
            elif prev_time <= 0:
                now = 0
            else:
                now = prev_time
        elif command == "next":
            next_time = now + 10
            if next_time >= start and next_time <= end:
                now = end
            elif next_time >= video:
                now = video
            else:
                now = next_time
                
    answer = str(now // 60).zfill(2) + ":" + str(now % 60).zfill(2)
    return answer