import threading
import xml.etree.ElementTree as et

def getdata(filename):
	xmltree=et.parse(filename)
	root= xmltree.getroot()
	print root.tag
	a=[]	
	for child in root:
		a.append(int(child.text))
		print child.tag, child.text
	print a
	return a

def partition(first, last):
	pivot=a[first]
	i=first+1
	j=last
	while i<=j:		
		while i<len(a) and a[i]<=pivot:
			i+=1
		while a[j]>pivot:
			j-=1
		if i<j:
			a[i], a[j]=a[j], a[i]
	a[first], a[j]=a[j], pivot
	return j


def quicksort(first, last):
	if first<=last:
		mid=partition(first, last)
		print threading.current_thread().getName(), "found mid at ", mid
		quicksort(first, mid-1)
		quicksort(mid+1, last)
		t1=threading.Thread(target=quicksort, args=(first, mid-1))
		t2=threading.Thread(target=quicksort, args=(mid+1, last))
		t1.start()
		t2.start()
		t1.join()
		t2.join()

a=getdata("input.xml")
quicksort(0, len(a)-1)
print a
		


