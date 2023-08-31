import geemap


def GetCoveringGrid(outputDataFolder, RoI, override=False):
    coveringGridPath = outputDataFolder/'Shapefiles'/'CoveringGrid.shp'
    coveringGridPath.parent.mkdir(exist_ok=True, parents=True)

    if (not coveringGridPath.exists()) or override:
        geemap.ee_to_shp(RoI.coveringGrid('EPSG:4326', 500*32), coveringGridPath.as_posix())
        

    coveringGrid = geemap.shp_to_ee(coveringGridPath.as_posix())
    
    listSize = coveringGrid.size().getInfo()
    coveringGridList = coveringGrid.toList(listSize)

    return listSize, coveringGridList