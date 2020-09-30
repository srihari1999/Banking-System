import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime
import tkinter.font as font

def is_number(s):
	try:
		float(s)
		return 1
	except ValueError:
		return 0
	




def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write_create(master,name,oc,pin,branch,phno):
	
	
#	print(len(oc))

	if(is_number(name) or name == ""):
		messagebox.showinfo("Error","Invalid Name \nPlease Provide Valid Name.")
		master.destroy()
		return 

	if(oc == "" or len(oc) > 9):
		messagebox.showinfo("Error", "Credit Amount cannot be Zero(0)\nMax Amount Allowed is 99999." )	
		master.destroy()
		return	


	if(oc == "" or len(oc) < 4):
		messagebox.showinfo("Error", "Pin Is Required with Minimum 4 Charcters" )	
		master.destroy()
		return	

	
	if(is_number(branch) or name == ""):
		messagebox.showinfo("Error","Invalid Branch Name\nPlease Provide Valid Branch Name.")
		master.destroy()
		return 

	if(len(phno)!=10 or phno == ""):
		messagebox.showinfo("Error","Invalid Phone Number\nPlease Provide Valid Phone Number.")
		master.destroy()
		return 




	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.write(branch+"\n")
	fdet.write(phno+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date and Time\tCredit\tDebit\tBalance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+oc+"\t"+str(0)+"\t"+oc+"\n")
	frec.close()
	
	fmes=open(str(accnt_no)+"-mess.txt",'w')
	fmes.write("Date and Time\tSent_By\tReceived_By\tMessage\n")
	fmes.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return





def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()

	fmes=open(str(accnt_no)+"-mess.txt",'w')
	fmes.write("Date and Time\tSent_By\tReceived_By\tMessage\n")
	fmes.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return





def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+str(amti)+"\t"+str(0)+"\t"+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return





def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+str(0)+"\t"+str(amti)+"\t"+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

	
	
def transfer_crdt_write(amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+str(amti)+"\t"+str(0)+"\t"+str(cb)+"\n")
	frec.close()
	return


	
	
def transfer_debit_write(master,amt,accnt,accnt1,nm):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	account=fdet.readline()
	name=fdet.readline()
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+str(0)+"\t"+str(amti)+"\t"+str(cb)+"\n")
		frec.close()
		transfer_crdt_write(amt,accnt1,nm)
		messagebox.showinfo("Operation Successfull!!","Amount Transferred Successfully!!")
		master.destroy()
		return
	
	
	
	
	
	
def Cr_Amt(accnt,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x400")
	creditwn.title("Credit Amount")
	creditwn.configure(bg='#8AAEC6')
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","30","bold"))
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",text="Amount:",height=1,padx=10,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	e1=tk.Entry(creditwn,relief="raised")
	l1.place(x=170,y=130)
	e1.place(x=300,y=130,height=28,width=180)
	e1.config(font=("Courier","17","bold"))
	myF = font.Font(family='Helvetica', size=20, weight='bold')
	b=tk.Button(creditwn,text="CREDIT",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name),height=1,bg="#C21807",fg="white")
	b['font'] = myF
	b.place(x=245,y=175,height=23,width=100)
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


	
	
def De_Amt(accnt,name):
	debitwn=tk.Tk()
	debitwn.geometry("600x400")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg='#8AAEC6')
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","30","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="raised",text="Amount:",height=1,padx=10,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	e1=tk.Entry(debitwn,relief="raised")
	l1.place(x=170,y=130)
	e1.place(x=300,y=130,height=28,width=180)
	e1.config(font=("Courier","17","bold"))
	myF = font.Font(family='Helvetica', size=20, weight='bold')
	b=tk.Button(debitwn,text="DEBIT",relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name),bg="#C21807",fg="white")
	b.place(x=250,y=175,height=23,width=100)
	b['font']=myF
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




def disp_bal(accnt):
	disp=tk.Tk()
	disp.geometry("600x400")
	disp.title("Balance")	
	disp.configure(bg='#8AAEC6')
	l_title=tk.Message(disp,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","30","bold"))
	l_title.pack(side="top")
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	l1=tk.Label(disp,relief="raised",text="Balance:",height=1,padx=10,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l1.place(x=170,y=130)
	l2=tk.Label(disp,text=bal,font=("Courier","15","bold"),anchor="center",bg='#8AAEC6')
	l2.place(x=300,y=130)
	fdet.close()
	
	#messagebox.showinfo("Balance",bal)




def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("600x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg='#8AAEC6')
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Transaction History:",padx=100,pady=10,width=600,bg="orange",fg="white",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	y1=120
	for line in frec:
		word=line.split('\t')
		l1=tk.Label(disp_wn,anchor="center",text=word[0],relief="raised",bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l1.place(x=50,y=y1,width=200,height=30)
		l2=tk.Label(disp_wn,anchor="center",text=word[1],relief="raised",width=350,bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l2.place(x=250,y=y1,width=100,height=30)
		l3=tk.Label(disp_wn,anchor="center",text=word[2],relief="raised",width=350,bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l3.place(x=350,y=y1,width=100,height=30)
		l4=tk.Label(disp_wn,anchor="center",text=word[3].strip('\n'),relief="raised",width=350,bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l4.place(x=450,y=y1,width=100,height=30)
		y1=y1+30
	y1=y1+10
	myF1 = font.Font(family='Helvetica', size=18, weight='bold')
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy,fg="white",bg="#C21807")
	b.place(x=280,y=y1)
	b['font']=myF1
	frec.close()


def disp_message(accnt):
	"Inbox of the user too display the message"
	disp_wn=tk.Tk()
	disp_wn.geometry("600x600")
	disp_wn.title("Inbox")
	disp_wn.configure(bg='#8AAEC6')
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Inbox History:",padx=100,pady=10,width=600,bg="orange",fg="white",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	fre=open(accnt+"-mess.txt",'r')
	y1=120
	for line in fre:
		word=line.split('\t')
		l1=tk.Label(disp_wn,anchor="center",text=word[0],relief="raised",bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l1.place(x=50,y=y1,width=200,height=30)
		l2=tk.Label(disp_wn,anchor="center",text=word[1],relief="raised",width=350,bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l2.place(x=250,y=y1,width=100,height=30)
		l3=tk.Label(disp_wn,anchor="center",text=word[2],relief="raised",width=350,bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l3.place(x=350,y=y1,width=100,height=30)
		l4=tk.Label(disp_wn,anchor="center",text=word[3].strip('\n'),relief="raised",bg="#004c8f",fg="white",font=("Courier","10","bold"))
		l4.place(x=450,y=y1,width=100,height=30)
		y1=y1+30
	y1=y1+10
	myF1 = font.Font(family='Helvetica', size=18, weight='bold')
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy,fg="white",bg="#C21807")
	b.place(x=280,y=y1)
	b['font']=myF1
	fre.close()

def transfer1(accnt):

	transfer=tk.Tk()
	transfer.geometry("600x600")
	transfer.title("Tranfer")
	transfer.configure(bg='#8AAEC6')
	#fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(transfer,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(transfer,text="Name",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l1.place(x=110,y=130)
	#l1.pack(side="top")
	e1=tk.Entry(transfer)
	e1.place(x=350,y=130,width=180,height=28)
	e1.config(font=("Courier","15","bold"))
	#e1.pack(side="top")
	l2=tk.Label(transfer,text="Account number",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l2.place(x=110,y=180)
	#l2.pack(side="top")
	e2=tk.Entry(transfer)
	e2.place(x=350,y=180,width=180,height=28)
	e2.config(font=("Courier","15","bold"))
	#e2.pack(side="top")
	l3=tk.Label(transfer,text="Amount",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l3.place(x=110,y=230)
	#l3.pack(side="top")
	e3=tk.Entry(transfer)
	e3.place(x=350,y=230,width=180,height=28)
	e3.config(font=("Courier","15","bold"))
	#e3.pack(side="top")
	myF1 = font.Font(family='Helvetica', size=18, weight='bold')
	b=tk.Button(transfer,text="TRANSFER",command=lambda: transfer_debit_write(transfer,e3.get(),accnt,e2.get(),e1.get()),bg="#C21807",fg="white")
	b.place(x=270,y=280,width=115,height=26)
	b['font']=myF1
	#b.pack(side="top")
	#b1=tk.Button(text="HOME",relief="raised",bg="black",fg="white",command=lambda: home_return(transfer))
	#b1.place(x=380,y=280,width=100,height=23)
	#b1.pack(side="top")
	#transfer.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))   
	

'message funtion to send message to other account'    

def transfer2(accnt):

	transfer=tk.Tk()
	transfer.geometry("600x600")
	transfer.title("Message Box")
	transfer.configure(bg='#8AAEC6')
	#fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(transfer,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(transfer,text="Name",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l1.place(x=110,y=130)
	#l1.pack(side="top")
	e1=tk.Entry(transfer)
	e1.place(x=350,y=130,width=180,height=28)
	e1.config(font=("Courier","15","bold"))
	#e1.pack(side="top")
	l2=tk.Label(transfer,text="Account number",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l2.place(x=110,y=180)
	#l2.pack(side="top")
	e2=tk.Entry(transfer)
	e2.place(x=350,y=180,width=180,height=28)
	e2.config(font=("Courier","15","bold"))
	#e2.pack(side="top")
	l3=tk.Label(transfer,text="Message",relief="raised",height=2,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l3.place(x=110,y=230)
	#l3.pack(side="top")
	e3=tk.Entry(transfer)
	e3.place(x=350,y=230,width=180,height=50)
	e3.config(font=("Courier","15","bold"))
	#e3.pack(side="top")
	myF1 = font.Font(family='Helvetica', size=18, weight='bold')
	b=tk.Button(transfer,text="SEND",command=lambda: transfer_message(transfer,e3.get(),accnt,e2.get(),e1.get()),bg="#C21807",fg="white")
	b.place(x=270,y=340,width=115,height=26)
	b['font']=myF1

def transfer_message(master,mess,accnt,accnt1,nm):

	if(mess == ""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return

	fmes = open(str(accnt1)+"-mess.txt",'a+')
	fmes.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+str(accnt)+"\t"+str(accnt1)+"\t"+str(mess)+"\n")
	fmes.close()
	messagebox.showinfo("Details","Message Sent to Account Number:"+str(accnt1))
	master.destroy()
	return
	# pin=fdet.readline()
	# camt=int(fdet.readline())
	# account=fdet.readline()
	# name=fdet.readline()
	# fdet.close()
	# if(int(amt)>camt):
	#     messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	# else:
	#     amti=int(amt)
	#     cb=camt-amti
	#     fdet=open(accnt+".txt",'w')
	#     fdet.write(pin)
	#     fdet.write(str(cb)+"\n")
	#     fdet.write(accnt+"\n")
	#     fdet.write(name+"\n")
	#     fdet.close()
	#     frec=open(str(accnt)+"-rec.txt",'a+')
	#     frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]",gmtime()))+"\t"+str(0)+"\t"+str(amti)+"\t"+str(cb)+"\n")
	#     frec.close()
	#     transfer_crdt_write(amt,accnt1,nm)
	#     messagebox.showinfo("Operation Successfull!!","Amount Transferred Successfully!!")
	#     master.destroy()
	#     return 
def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("1920x1080")
	rootwn.title("UNITED BANK-"+name)
	rootwn.configure(background='#8AAEC6')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	
	l_title=tk.Message(rootwn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	myFnt = font.Font(family='Helvetica', size=12, weight='bold')
	label=tk.Label(text="Active User: "+name,relief="raised",bg="green",fg="white",anchor="center",justify="center",padx=20,height=1)
	label.pack(side="top")
	label['font'] = myFnt
	""""img2=tk.PhotoImage(file="button_credit1.png")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="button_debit1.png")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="button_balance1.png")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="button_transactions1.png")
	myimg5=img5.subsample(2,2)
	img7=tk.PhotoImage(file="button_pay.png")
	myimg7=img7.subsample(2,2)"""
	myFont = font.Font(family='Helvetica', size=20, weight='bold')
	b2=tk.Button(text="Credit",command=lambda: Cr_Amt(accnt,name),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b2['font'] = myFont
	b3=tk.Button(text="Debit",command=lambda: De_Amt(accnt,name),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b3['font'] = myFont
	b4=tk.Button(text="Balance",command=lambda: disp_bal(accnt),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b4['font'] = myFont
	b5=tk.Button(text="History",command=lambda: disp_tr_hist(accnt),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b5['font'] = myFont
	b7=tk.Button(text="Pay",command=lambda: transfer1(accnt),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b7['font'] = myFont
	b8=tk.Button(text="Send Message",command=lambda: transfer2(accnt),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b8['font'] = myFont
	b9=tk.Button(text="Inbox",command=lambda: disp_message(accnt),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b9['font'] = myFont
	#img6=tk.PhotoImage(file="button_logout1.png")
	#myimg6=img6.subsample(2,2)
	b6=tk.Button(text="Logout",command=lambda: logout(rootwn),border=0,bg='#004c8f',fg='red',height=1,width=11)
	b6['font'] = myFont
	b2.place(x=360,y=150)
	b3.place(x=360,y=220)
	b4.place(x=800,y=150)
	b5.place(x=800,y=220)
	b6.place(x=575,y=500)
	b7.place(x=575,y=420)
	b8.place(x=360,y=300)
	b9.place(x=800,y=300)



	
	
	
	
##uyfkuf
	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

	
	
	
	
def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)

		
		
		
		

def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("600x600")
	loginwn.title("Log in")
	loginwn.configure(bg="#588BAE")
	#fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Enter Name",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l1.place(x=110,y=130)
	#l1.pack(side="top")
	e1=tk.Entry(loginwn)
	e1.place(x=350,y=130,width=180,height=28)
	e1.config(font=("Courier","15","bold"))
	#e1.pack(side="top")
	l2=tk.Label(loginwn,text="Account number",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l2.place(x=110,y=180)
	#l2.pack(side="top")
	e2=tk.Entry(loginwn)
	e2.place(x=350,y=180,width=180,height=28)
	e2.config(font=("Courier","15","bold"))
	#e2.pack(side="top")
	l3=tk.Label(loginwn,text="PIN",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l3.place(x=110,y=230)
	#l3.pack(side="top")
	e3=tk.Entry(loginwn,show="*")
	e3.place(x=350,y=230,width=180,height=28)
	e3.config(font=("Courier","15","bold"))
	#e3.pack(side="top")
	mF = font.Font(family='Helvetica', size=14, weight='bold')
	b=tk.Button(loginwn,text="LOGIN",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()),bg="#C21807",fg="white")
	b.place(x=150,y=280,width=100,height=26)
	b['font'] = mF
	#b.pack(side="top")
	b1=tk.Button(text="HOME",relief="raised",bg="black",fg="white",command=lambda: home_return(loginwn))
	b1.place(x=390,y=280,width=100,height=26)
	b1['font'] = mF
	#b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	

	
	
	
	
def Create():
	
	crwn=tk.Tk()
	crwn.geometry("600x600")
	crwn.resizable(width="False",height="False")
	crwn.title("Create Account")
	crwn.configure(bg="#588BAE")
	#fr1=tk.Frame(crwn,bg="blue")
	l_title=tk.Message(crwn,text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="Name",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	#l1.pack(side="top")
	l1.place(x=110,y=130)
	e1=tk.Entry(crwn)
	e1.place(x=350,y=130,width=180,height=28)
	e1.config(font=("Courier","15","bold"))
	#e1.pack(side="top")
	l2=tk.Label(crwn,text="Opening credit",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l2.place(x=110,y=180)
	#l2.pack(side="top")
	e2=tk.Entry(crwn)
	e2.place(x=350,y=180,width=180,height=28)
	e2.config(font=("Courier","15","bold"))
	#e2.pack(side="top")
	l3=tk.Label(crwn,text="PIN",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l3.place(x=110,y=230)
	#l3.pack(side="top")
	e3=tk.Entry(crwn,show="*")
	e3.place(x=350,y=230,width=180,height=28)
	e3.config(font=("Courier","15","bold"))
	#e3.pack(side="top")
	l4=tk.Label(crwn,text="Branch",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l4.place(x=110,y=280)
	#l4.pack(side="top")
	e4=tk.Entry(crwn)
	e4.place(x=350,y=280,width=180,height=28)
	e4.config(font=("Courier","15","bold"))
	#e4.pack(side="top")
	l5=tk.Label(crwn,text="Customer Number",relief="raised",height=1,width=15,font=("Courier","15","bold"),bg="#004c8f",fg="white")
	l5.place(x=110,y=330)
	#l5.pack(side="top")
	e5=tk.Entry(crwn)
	e5.place(x=350,y=330,width=180,height=28)
	e5.config(font=("Courier","15","bold"))
	#e5.pack(side="top")
	myFo = font.Font(family='Helvetica', size=20, weight='bold')
	b=tk.Button(crwn,text="Create",command=lambda: write_create(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip(), e4.get().strip(), e5.get().strip()),bg="#C21807",fg="white")
	b.place(x=280,y=380)
	b['font'] = myFo
	#b.pack(side="top")
	crwn.bind("<Return>",lambda x:write_create(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip(), e4.get().strip(),e5.get().strip()))
	return









def Main_Menu():
	

	rootwn=tk.Tk()
	rootwn.geometry("1920x1080")
	rootwn.title("UNITED Bank")
	rootwn.configure(background='orange')
	#rootwn.resizable(width="False",height="False")
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="pile1.gif")
	x = tk.Label (image = bg_image)
	x.place(y=-400)
	l_title=tk.Message(text="ALVA'S BANK",relief="raised",width=2000,padx=600,pady=-10,fg="white",bg="#C21807",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")	


	#l_title1=tk.Message(text="Shri hari Mera Paisa Kab Deka",relief="raised",width=1000,padx=200,pady=-10,fg="white",bg="#C21807",justify="left",anchor="nw")
	#l_title1.config(font=("Courier","40","italic"))
	#l_title1.pack(side="top")

	""""imgc1=tk.PhotoImage(file="button_new-account1.png")
	imglo=tk.PhotoImage(file="button_login1.png")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)"""

	#b1=tk.Button(image=imgc,command=Create,border=0,width=200)
	#b1.image=imgc
	#b1.pack()
	myFont = font.Font(family='Helvetica', size=20, weight='bold')
	b1=tk.Button(text="New Account",command=Create,border=0,bg='#004c8f',fg='red',height=1,width=11)
	b1['font'] = myFont
	b2=tk.Button(text="Login",command=lambda: log_in(rootwn),border=0,fg='red',bg='#004c8f',height=1,width=11)
	b2['font'] = myFont
	#b2.image=imglog
	#img6=tk.PhotoImage(file="button_quit.png")
	#myimg6=img6.subsample(2,2)

	b6=tk.Button(text="QUIT",command=rootwn.destroy,border=0,bg='#004c8f',fg='red',height=1,width=11)
	b6['font'] = myFont
	#b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=800,y=400)

	rootwn.mainloop()

Main_Menu()