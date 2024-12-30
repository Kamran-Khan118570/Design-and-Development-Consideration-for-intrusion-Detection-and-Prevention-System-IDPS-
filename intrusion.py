import cv2
from cvzone.PoseModule import PoseDetector
detector=PoseDetector()
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cols ="""duration,
protocol_type,
service,
flag,
src_bytes,
dst_bytes,
land,
wrong_fragment,
urgent,
hot,
num_failed_logins,
logged_in,
num_compromised,
root_shell,
su_attempted,
num_root,
num_file_creations,
num_shells,
num_access_files,
num_outbound_cmds,
is_host_login,
is_guest_login,
count,
srv_count,
serror_rate,
srv_serror_rate,
rerror_rate,
srv_rerror_rate,
same_srv_rate,
diff_srv_rate,
srv_diff_host_rate,
dst_host_count,
dst_host_srv_count,
dst_host_same_srv_rate,
dst_host_diff_srv_rate,
dst_host_same_src_port_rate,
dst_host_srv_diff_host_rate,
dst_host_serror_rate,
dst_host_srv_serror_rate,
dst_host_rerror_rate,
dst_host_srv_rerror_rate"""
while True:
    success,img=cap.read()
    img=detector.findPose(img)
    imlist,bbox=detector.findPosition(img)

    if len(imlist)> 0:
        print("Human Detect")
        cv2.imshow("Output",img)
    q=cv2.waitKey(1)

