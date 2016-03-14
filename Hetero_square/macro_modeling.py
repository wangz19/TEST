# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def square(side_length, mesh_size, engineering_strain):
    ###-------------------
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    ###--------------------------

    ###--------parameters----------
    side = side_length
    m = mesh_size
    strain = engineering_strain
    ###----------------------------

    ### ---physical modeling---
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(-side/2, side/2), point2=(side/2, -side/2))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)

    ### --- initial material ---
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((27000.0, 0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=m, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()

    ### -------- map mesh and model into assembly-----------
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    a.Instance(name='Part-1-1', part=p, dependent=ON)

    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Set(edges=edges1, name='Set-1')
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#8 ]', ), )
    region = a.Set(edges=edges1, name='Set-2')
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
        region=region, u1=5.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)