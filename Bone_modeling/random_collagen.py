# - * - coding: UTF-8 - * -
	#filename:abaqus_1.py
	# this create random circle in rectangular box
from random import*           
from abaqus import*  	
from abaqusConstants import *
import mesh

def RandomFunc(percent,n,Dispersion,E1, MU1,E2, MU2,size0,x0,y0):
			## Vf 纤维体积含量，collagen fibril number, 
	Mdb()
	##############################随机生成纤维束的圆心坐标xy
	r0=(percent*x0*y0/(n*3.14))**0.5  #mean value of radius
	r=r0+Dispersion
#### 将边界扩大到可能的范围，在范围内去任意圆心位置，在范围内随机分布 random dispersion
	x=(x0-2*r+4*r0)*random()+r-2*r0
	y=(y0-2*r+4*r0)*random()+r-2*r0
	xy=[(x,y)]
	
	if(x<r0)and((y-r0)*(y0-r0-y)>0): #区域1
		xy.append((x+x0,y))
	elif(x>x0-r0)and((y-r0)*(y0-r0-y)>0):
		xy.append((x-x0,y))		
	elif(y<r0)and((x-r0)*(x0-r0-x)>0):
		xy.append((x,y+y0))
	elif(y>y0-r0)and((x-r0)*(x0-r0-x)>0):
		xy.append((x,y-y0))	
	elif(x<r0)and(y<r0):	
		xy.append((x+x0,y))	
		xy.append((x,y+y0))	
		xy.append((x+x0,y+y0))			
	elif(x<r0)and(y>(y0-r0)):		
		xy.append((x+x0,y))
		xy.append((x,y-y0))	
		xy.append((x+x0,y-y0))			
	elif(x>(x0-r0))and(y<r0):		
		xy.append((x-x0,y))	
		xy.append((x,y+y0))	
		xy.append((x-x0,y+y0))	
	elif(x>(x0-r0))and(y>(y0-r0)):	
		xy.append((x,y-y0))	
		xy.append((x-x0,y))	
		xy.append((x-x0,y-y0))	
	
	for i in range(n-1):
		flag=1
		while flag==1:
			x=(x0-2*r+4*r0)*random()+r-2*r0
			y=(y0-2*r+4*r0)*random()+r-2*r0
			flag=0
			flag2=0
			flag3=0
			flag4=0
			dis2=1000.0
			dis3=1000.0
			dis4=1000.0
			for j in range(len(xy)):
			
				dis=(x-xy[j][0])**2+(y-xy[j][1])**2
				if(x<r0)and((y-r0)*(y0-r0-y)>0):
					flag2=1
					x1=x+x0
					y1=y
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
				elif(x>x0-r0)and((y-r0)*(y0-r0-y)>0):
					flag2=1
					x1=x-x0
					y1=y	
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
				elif(y<r0)and((x-r0)*(x0-r0-x)>0):
					flag2=1
					x1=x
					y1=y+y0
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
				elif(y>y0-r0)and((x-r0)*(x0-r0-x)>0):
					flag2=1
					x1=x
					y1=y-y0			
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
					
				elif(x<r0)and(y<r0):		
					flag2=1
					x1=x+x0
					y1=y		
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
					
					flag3=1
					x2=x
					y2=y+y0		
					dis3=(x2-xy[j][0])**2+(y2-xy[j][1])**2
					
					flag4=1
					x3=x+x0
					y3=y+y0		
					dis4=(x3-xy[j][0])**2+(y3-xy[j][1])**2					
				elif(x<r0)and(y>(y0-r0)):		

					flag2=1
					x1=x+x0
					y1=y		
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
					
					flag3=1
					x2=x
					y2=y-y0			
					dis3=(x2-xy[j][0])**2+(y2-xy[j][1])**2
					
					flag4=1
					x3=x+x0
					y3=y-y0			
					dis4=(x3-xy[j][0])**2+(y3-xy[j][1])**2			
				elif(x>(x0-r0))and(y<r0):		
					flag2=1
					x1=x-x0
					y1=y		
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
					
					flag3=1
					x2=x
					y2=y+y0		
					dis3=(x2-xy[j][0])**2+(y2-xy[j][1])**2
					
					flag4=1
					x3=x-x0
					y3=y+y0			
					dis4=(x3-xy[j][0])**2+(y3-xy[j][1])**2	
				elif(x>(x0-r0))and(y>(y0-r0)):				
					flag2=1
					x1=x
					y1=y-y0			
					dis2=(x1-xy[j][0])**2+(y1-xy[j][1])**2
					
					flag3=1
					x2=x-x0
					y2=y		
					dis3=(x2-xy[j][0])**2+(y2-xy[j][1])**2
					
					flag4=1
					x3=x-x0
					y3=y-y0			
					dis4=(x3-xy[j][0])**2+(y3-xy[j][1])**2	
					
				if (dis<((2*r)**2+Dispersion))or(dis2<((2*r)**2+Dispersion))or(dis3<((2*r)**2+Dispersion))or(dis4<((2*r)**2+Dispersion)):
					flag=1
		xy.append((x,y))
		if flag2==1:
			xy.append((x1,y1))
		if flag3==1:
			xy.append((x2,y2))	
		if flag4==1:
			xy.append((x3,y3))		
	
	##############################开始建模
	#第一步, 建立建模
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=10.0)   #定义模型的草图s
	s.rectangle(point1=(0.0, 0.0), point2=(x0, y0))                   #指定两顶点画矩形
	p = mdb.models['Model-1'].Part(name='Part-1',dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)   #定义模型的部件part-1
	p.BaseShell(sketch=s)                                                        #将s赋给p
			

	s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile_1_', sheetSize=100.0)

	for i in range(len(xy)):
		s1.CircleByCenterPerimeter(center=xy[i], point1=(xy[i][0]+r0,xy[i][1]))      #指定圆心和圆上一点画圆n个
	p1 = mdb.models['Model-1'].parts['Part-1']
	pickedFaces = p1.faces[0:1]
	p1.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)

	#第二步, 材料定义
	mdb.models['Model-1'].Material(name='Material-1')   #定义材料名称1
	mdb.models['Model-1'].materials['Material-1'].Elastic(table=((E1, MU1), ))  #定义材料1的刚度
	mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1',material='Material-1',thickness=1.0)  #定义截面2

	mdb.models['Model-1'].Material(name='Material-2')   #定义材料名称2
	mdb.models['Model-1'].materials['Material-2'].Elastic(table=((E2, MU2), ))  #定义材料2的刚度
	mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2',material='Material-2',thickness=1.0)  #定义截面2

	faces = mdb.models['Model-1'].parts['Part-1'].faces.findAt(((Dispersion*0.5, Dispersion*0.5, 0.0), ))
	region =(faces, )     #以上两行找到包含点（0,0,0）的面，保存到region 
	mdb.models['Model-1'].parts['Part-1'].SectionAssignment(region=region, sectionName='Section-1') #截面属性附给选中的面region 

	f2=mdb.models['Model-1'].parts['Part-1'].faces
	for i in range(len(f2)):
		if f2[i:i+1]==faces:
			j=i
	faces2=f2[0:j]+f2[j+1:len(f2)]
	region2 =(faces2, )     #以上找到除faces以外的面，保存到region2 
	mdb.models['Model-1'].parts['Part-1'].SectionAssignment(region=region2, sectionName='Section-2') #截面属性2附给选中的面region2 

	#第三步，装配
	a1 = mdb.models['Model-1'].rootAssembly
	p = mdb.models['Model-1'].parts['Part-1']  #指定part-1
	a1.Instance(name='Part-1-1', part=p, dependent=OFF) #生成part-1对象的实体Part-1-1，independent网格在Instance上面

	#第四步, 定义分析步
	mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial',
		timeIncrementationMethod=FIXED, initialInc=0.01, noStop=OFF)  #定义一个固定增量的静态分析步
	mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValuesInStep(stepName='Step-1',
		variables=('S', 'U'))  #定义输出到ODB文件的数据(应力、位移)

	#第五步, 网格划分控制
	elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
	faces = mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces[0:n+1]
	pickedRegions =(faces, )
	mdb.models['Model-1'].rootAssembly.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))   #定义两种网格类型

	pickedEdges=a1.instances['Part-1-1'].edges
	a1.seedEdgeBySize(edges=pickedEdges, size=size0,constraint=FIXED) #撒网格种子
	partInstances =(a1.instances['Part-1-1'], )
	a1.generateMesh(regions=partInstances) #给partInstances划分网格

	#第六步, 定义多点约束条件-----MPC
	m=mdb.models['Model-1']
	r=m.rootAssembly
	node=r.instances['Part-1-1'].nodes
	ne=[]    #ne 存储所有边界上的单元节点的编号
	for i in range(len(node)):
		x=node[i].coordinates[0]
		y=node[i].coordinates[1]
		flag=(x-x0)*(x-0)*(y-y0)*(y-0)*10000
		if abs(flag)<0.0001:
			ne.append(i)
	print "boundary nodes ne0=", len(ne)

	for i in range(len(ne)):     #找出四个顶点
		x=node[ne[i]].coordinates[0]
		y=node[ne[i]].coordinates[1]
		if (abs(x-0)<0.0001)and(abs(y-0)<0.0001):
			r.Set(nodes=node[ne[i]:ne[i]+1],name='set-01')
			aa1=i
		elif(abs(x-x0)<0.0001)and(abs(y-0)<0.0001):
			r.Set(nodes=node[ne[i]:ne[i]+1],name='set-02')
			aa2=i
		elif(abs(x-0)<0.0001)and(abs(y-y0)<0.0001):
			r.Set(nodes=node[ne[i]:ne[i]+1],name='set-03')
			aa3=i
		elif(abs(x-x0)<0.0001)and(abs(y-y0)<0.0001):
			r.Set(nodes=node[ne[i]:ne[i]+1],name='set-04')
			aa4=i
	aa=[aa1,aa2,aa3,aa4]
	aa.sort()
	# 从边界点集合中删除顶点
	del ne[aa[3]];del ne[aa[2]];del ne[aa[1]];del ne[aa[0]]
	#print a1,a2,a3,a4
	print "ne1=", len(ne)
	m.Equation(name='eq-00',terms=((1,'set-04',1),(-1,'set-02',1),(-1,'set-03',1))) #定义角点的MPC
	m.Equation(name='eq-01',terms=((1,'set-04',2),(-1,'set-02',2),(-1,'set-03',2)))

	#-----------------------------定义其他边界点的MPC----------------
	xx=x0
	yy=y0
	i=0
	for n in range(len(ne)):
		x0=node[ne[n]].coordinates[0]
		y0=node[ne[n]].coordinates[1]
		for j in range(n+1,len(ne)):
			x1=node[ne[j]].coordinates[0]
			y1=node[ne[j]].coordinates[1]
			if (abs(x0-x1)<0.3*size0)and(abs(abs(y0-y1)-yy)<0.00001)or(abs(y0-y1)<0.3*size0)and(abs(abs(x0-x1)-xx)<0.00001):
				r.Set(nodes=node[ne[n]:ne[n]+1],name='set'+str(2*i+1))
				r.Set(nodes=node[ne[j]:ne[j]+1],name='set'+str(2*i+2))
				if abs(y0-yy)<0.00001:
					m.Equation(name='eq'+str(2*i+1),terms=((1,'set'+str(2*i+1),1),(-1,'set-03',1),(-1,'set'+str(2*i+2),1)))
					m.Equation(name='eq'+str(2*i+2),terms=((1,'set'+str(2*i+1),2),(-1,'set-03',2),(-1,'set'+str(2*i+2),2)))
				elif abs(y1-yy)<0.00001:
					m.Equation(name='eq'+str(2*i+1),terms=((1,'set'+str(2*i+2),1),(-1,'set-03',1),(-1,'set'+str(2*i+1),1)))
					m.Equation(name='eq'+str(2*i+2),terms=((1,'set'+str(2*i+2),2),(-1,'set-03',2),(-1,'set'+str(2*i+1),2)))
				elif abs(x0-xx)<0.00001:
					m.Equation(name='eq'+str(2*i+1),terms=((1,'set'+str(2*i+1),1),(-1,'set-02',1),(-1,'set'+str(2*i+2),1)))
					m.Equation(name='eq'+str(2*i+2),terms=((1,'set'+str(2*i+1),2),(-1,'set-02',2),(-1,'set'+str(2*i+2),2)))
				elif abs(x1-xx)<0.00001:
					m.Equation(name='eq'+str(2*i+1),terms=((1,'set'+str(2*i+2),1),(-1,'set-02',1),(-1,'set'+str(2*i+1),1)))
					m.Equation(name='eq'+str(2*i+2),terms=((1,'set'+str(2*i+2),2),(-1,'set-02',2),(-1,'set'+str(2*i+1),2)))
				i=i+1
				break
	print "i=",i    
	#--------------------------------------------------------------    
	#第七步, 荷载边界定义
	m=mdb.models['Model-1']                  
	region = m.rootAssembly.sets['set-01']    #选中固支节点，保存到region
	m.DisplacementBC(name='BC-1', createStepName='Initial',region=region,
		u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, localCsys=None) 
	#定义固支边界
	region = m.rootAssembly.sets['set-02']    #选中简支节点，保存到region
	m.DisplacementBC(name='BC-2', createStepName='Initial',region=region,
		u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, localCsys=None) #定义简支边界

	region = m.rootAssembly.sets['set-03']    #选中加载节点，保存到region
	m.DisplacementBC(name='BC-3', createStepName='Step-1',region=region,
		u1=UNSET, u2=1.0, ur3=UNSET, amplitude=UNSET, fixed=OFF,localCsys=None) #定义位移载荷



	#-----------------------------------------第八步，生成任务以及其他杂项功能
	#mdb.models.changeKey(fromName='Model-1', toName='abaqus—001') #修改模型名称

	#mdb.models['Model-1'].materials['Material-1'].elastic.setValues(table=((514.3, 0.15),)) #修改模型中的材料属性
	jobname='Job-001'
	mdb.Job(name=jobname, model='Model-1', type=ANALYSIS, explicitPrecision=SINGLE, 
		nodalOutputPrecision=SINGLE, description='', 
		parallelizationMethodExplicit=DOMAIN, multiprocessingMode=DEFAULT, 
		numDomains=1, userSubroutine='', numCpus=1,  scratch='', 
		echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF) #生成任务

	#mdb.saveAs(pathName='c:/abaqus_workplace/abaqus-001.cae') #保存模型
	#mdb.jobs[jobname].submit() # 提交任务
	#mdb.jobs[jobname].waitForCompletion()  #计算完成后继续下面的语句
	#-----------------------------------------------------------

	#第九步，查看结果
	#	myViewport=session.viewports['Viewport: 1'] #显示
	#	myViewport.setValues(displayedObject=p)   
	#	myViewport.assemblyDisplay.setValues(mesh=ON)  	
	

RandomFunc(0.475 ,12, 0.01 ,80,0.3,200,0.28,0.03,1.732 ,1.0)

#RandomFunc(percent,n,Dispersion,E1, MU1,E2, MU2,size0,x0,y0)







