import cv2
import face_recognition
import laplacian_pyramid
import heart_rate_calculation
import eulerian

def calculation(path):
    # Frequency range for Fast-Fourier Transform
    freq_min = 1
    freq_max = 4

    # Preprocessing phase
    print("Reading and processing the video...")
    video_frames, frame_ct, fps = face_recognition.read_video(path)

    # Build Laplacian video pyramid
    print("Building Laplacian video pyramid...")
    lap_video = laplacian_pyramid.build_video_pyramid(video_frames)

    amplified_video_pyramid = []

    for i, video in enumerate(lap_video):
        if i == 0 or i == len(lap_video)-1:
            continue

        # Eulerian magnification with temporal FFT filtering
        print("Running FFT and Eulerian magnification...")
        result, fft, frequencies = eulerian.fft_filter(video, freq_min, freq_max, fps)
        lap_video[i] += result

        # Calculate heart rate
        print("Calculating heart rate...")
        heart_rate = heart_rate_calculation.find_heart_rate(fft, frequencies, freq_min, freq_max)

    # Collapse laplacian pyramid to generate final video
    #print("Rebuilding final video...")
    #amplified_frames = laplacian_pyramid.collapse_laplacian_video_pyramid(lap_video, frame_ct)

    # Output heart rate and final video
    print("Heart rate: ", heart_rate, "bpm")
    #print("Displaying final video...")

    #for frame in amplified_frames:
    #    cv2.imshow("frame", frame)
    #    cv2.waitKey(20)

    return heart_rate

#calculation("C:/Users/stamo/Downloads/video-1622273593_geo2.mp4")
