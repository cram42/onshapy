from onshapy import API, STLExportSettings
from onshapy.stl import StlResolution

onshape = API()
onshape.authorize()

# docs = client.findDocuments("*export*")
# for d in docs:
#     print("{}|{}|{}|{}".format(d.id, d.name, d.isPublic, d.link))

url = "https://cad.onshape.com/documents/b912b0dbc5f9764373497ed9/w/933e46a429cbd6978b9955d2/e/14720ce38a8ddadd2bd6d408"
url = onshape.decodeUrl(url)
if url.documentId:
    if url.workspaceId:
        if url.elementId:
            parts = onshape.getParts(url.documentId, url.workspaceId, url.elementId)
            if len(parts) > 0:
                part = parts[0]
                es = STLExportSettings()
                es.parts.append(part.id)
                es.resolution = StlResolution.COARSE
                stl = onshape.getSTL(url.documentId, url.workspaceId, url.elementId, es)
                fMode = "wb" if isinstance(stl, bytes) else "w"
                with open("tmp.stl", fMode) as f:
                    f.write(stl)

exit()
