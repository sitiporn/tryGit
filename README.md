# Test github<br />
Test1 Test2 Test3 Test4<br />
<br />
### สรุปคำสั่ง ตอนนี้ `24/08/2560`<br />
ใช้ git ในไฟล์โปรเจกเรา<br />
> git init

ดู status<br />
> git status

เเล้ว remote ไปที่ github repository ของเราที่สร้างเเล้ว<br />
> git remote add origin url...

ทำการ add file_code , tabเอา<br />
> git add file_name file_name2 ...

เมื่อมีการเเก้ไข code ที่ลองมาเเล้วต้อง add เเล้ว commit ก่อน<br />
> git commit -m "บอกไปว่ากำลังทำอะไร หรือเเก้อะไร"

จากนั้นก็ push ขึ้น server github ของเราได้ละ<br />
> git push -u origin master

ตามด้วย username and password<br />
จบส่วนการ update code ขึ้น github<br />
<br />
ส่วนการ pull หรือ load code ลงมาที่ local<br />
ตรวจดูการเปลี่ยนเเปลงก่อน<br />
> git fetch

จากนั้น merge มาหาโฟลเดอร์เรา<br />
> git merge origin/master

พอได้ไฟล์อัพเดทมาเเล้ว ลองดู status รู้สึกว่าต้อง add ก่อน<br />
เเต่ถ้ามีปัญหา Conflict ก็ต้องเเก้ก่อน อันนี้ยังงงๆ ว่ามัน conflict ตอนอัพไฟล์ขึ้นไปด้วยใช่ไหม?<br />
<br />
### คำสั่งอื่นๆ<br />
ดูประวัติ<br />
> git log

ดูเเละสร้าง branch<br />
> git branch 

หรือ สร้างเเละสลับในคำสังเดียว<br />
> git checkout -b branch_new_name

ลบ branch<br />
> git branch -d branch_name

สลับ branch<br />
> git checkout branch_name

ทำ merge ระหว่าง branch ได้ด้วย<br />
> git merge branch_name



