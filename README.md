# Test github
Test1 Test2 Test3 Test4 Test5 Test6

### สรุปคำสั่ง ตอนนี้ `24/08/2560`
ใช้ git ในไฟล์โปรเจกเรา
> git init

ดู status
> git status

เเล้ว remote ไปที่ github repository ของเราที่สร้างเเล้ว
> git remote add origin url...

ทำการ add file_code , tabเอา
> git add file_name file_name2 ...

เมื่อมีการเเก้ไข code ที่ลองมาเเล้วต้อง add เเล้ว commit ก่อน
> git commit -m "บอกไปว่ากำลังทำอะไร หรือเเก้อะไร"

จากนั้นก็ push ขึ้น server github ของเราได้ละ
> git push -u origin master

ตามด้วย username and password
จบส่วนการ update code ขึ้น github

ส่วนการ pull หรือ load code ลงมาที่ local
ตรวจดูการเปลี่ยนเเปลงก่อน
> git fetch

จากนั้น merge มาหาโฟลเดอร์เรา
> git merge origin/master

พอได้ไฟล์อัพเดทมาเเล้ว ลองดู status รู้สึกว่าต้อง add ก่อน
เเต่ถ้ามีปัญหา Conflict ก็ต้องเเก้ก่อน อันนี้ยังงงๆ ว่ามัน conflict ตอนอัพไฟล์ขึ้นไปด้วยใช่ไหม?

### คำสั่งอื่นๆ
ดูประวัติ
> git log

ดูเเละสร้าง branch
> git branch 

หรือ สร้างเเละสลับในคำสังเดียว
> git checkout -b branch_new_name

ลบ branch
> git branch -d branch_name

สลับ branch
> git checkout branch_name

ทำ merge ระหว่าง branch ได้ด้วย
> git merge branch_name

### การ fork, remote เพื่ออัพเดท เเละ pull requests กลับ origin/master
ทำการ fork เเล้วตั้งชื่อใหม่จะได้ไม่งง (เพิ่มเลข) (จริงๆดู owner ก็ได้)
จากนั้น clone มา local
> git clone url...

ทำการ remote เพื่ออัพเดทจากต้นฉบับ
> git remote add upstream url...

fetch เพื่อดูว่ามีอัพเดทไหม เเล้ว merge 
> git fetch upstream
> git merge upstream/master

จากนั้นถ้าต้องการอัพเดท repo ของเราเองที่ fork มา (เเละขอ pull requests ในหน้าเว็บดีกว่า)
> git add file_name
> git commit -m "text"
> git push origin master

หลังจากนั้นถ้าจะขอ pull requests ควรขอ merged กับ branch ย่อยจะดีที่สุดครับ

### โครงสร้าง git อย่างง่าย
โครงสร้างคำสั่ง คือ git ชื่อคำสั่ง คำสั่งย่อย(ถ้ามี) ชื่อไฟล์ หรือ remote_name branch_name
ตัวอย่าง
> git add file_name  

> git remote add remote_name url...  
> git remoet set-url remote_name url...  
> git push remote_name branch_name  
> git merge remote_name/branch_name  
> git felch remote_name  
> git status  

จบ...




