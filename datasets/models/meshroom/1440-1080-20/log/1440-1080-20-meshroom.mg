{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2019.2.0",
        "fileVersion": "1.1",
        "nodesVersions": {
            "CameraInit": "2.0",
            "Texturing": "5.0",
            "PrepareDenseScene": "3.0",
            "FeatureExtraction": "1.1",
            "StructureFromMotion": "2.0",
            "MeshFiltering": "2.0",
            "Meshing": "3.0",
            "DepthMapFilter": "3.0",
            "FeatureMatching": "2.0",
            "ImageMatching": "1.0",
            "DepthMap": "2.0"
        }
    },
    "graph": {
        "CameraInit_1": {
            "nodeType": "CameraInit",
            "position": [
                0,
                0
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 50,
                "split": 1
            },
            "uids": {
                "0": "2e79b7db50b91467eed1e5459f8c04c2c88c1c0c"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "viewpoints": [
                    {
                        "viewId": 9100444,
                        "poseId": 9100444,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0005.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 39228547,
                        "poseId": 39228547,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0039.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 53615480,
                        "poseId": 53615480,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0016.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 201379104,
                        "poseId": 201379104,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0035.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 215708560,
                        "poseId": 215708560,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0038.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 240072605,
                        "poseId": 240072605,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0048.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 244957115,
                        "poseId": 244957115,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0001.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 271657992,
                        "poseId": 271657992,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0018.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 294420513,
                        "poseId": 294420513,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0028.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 323690010,
                        "poseId": 323690010,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0029.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 333885708,
                        "poseId": 333885708,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0042.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 381804608,
                        "poseId": 381804608,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0047.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 457942114,
                        "poseId": 457942114,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0030.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 469853376,
                        "poseId": 469853376,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0044.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 598476991,
                        "poseId": 598476991,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0023.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 664385476,
                        "poseId": 664385476,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0022.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 670694811,
                        "poseId": 670694811,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0007.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 855031664,
                        "poseId": 855031664,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0049.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 861018912,
                        "poseId": 861018912,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0036.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 974967230,
                        "poseId": 974967230,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0006.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1009103060,
                        "poseId": 1009103060,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0033.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1117947081,
                        "poseId": 1117947081,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0026.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1133318834,
                        "poseId": 1133318834,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0003.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1164625911,
                        "poseId": 1164625911,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0002.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1176824930,
                        "poseId": 1176824930,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0010.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1251708541,
                        "poseId": 1251708541,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0046.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1309279213,
                        "poseId": 1309279213,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0031.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1374134381,
                        "poseId": 1374134381,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0011.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1377371419,
                        "poseId": 1377371419,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0019.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1385067319,
                        "poseId": 1385067319,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0043.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1397998855,
                        "poseId": 1397998855,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0004.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1427329861,
                        "poseId": 1427329861,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0025.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1458215115,
                        "poseId": 1458215115,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0034.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1471568385,
                        "poseId": 1471568385,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0012.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1560319651,
                        "poseId": 1560319651,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0037.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1593896531,
                        "poseId": 1593896531,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0050.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1595212049,
                        "poseId": 1595212049,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0020.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1599421579,
                        "poseId": 1599421579,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0017.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1630359084,
                        "poseId": 1630359084,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0008.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1740614238,
                        "poseId": 1740614238,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0015.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1757313003,
                        "poseId": 1757313003,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0045.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1800357838,
                        "poseId": 1800357838,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0013.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1839230745,
                        "poseId": 1839230745,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0009.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1994604610,
                        "poseId": 1994604610,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0027.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 1996197185,
                        "poseId": 1996197185,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0014.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 2010690355,
                        "poseId": 2010690355,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0040.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 2031696560,
                        "poseId": 2031696560,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0024.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 2056668188,
                        "poseId": 2056668188,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0021.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 2066217026,
                        "poseId": 2066217026,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0041.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    },
                    {
                        "viewId": 2125114409,
                        "poseId": 2125114409,
                        "path": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20/0032.jpg",
                        "intrinsicId": 2798600110,
                        "rigId": -1,
                        "subPoseId": -1,
                        "metadata": "{\"ImageDescription\": \"Lavc58.82.100\", \"PixelAspectRatio\": \"0.75\", \"ResolutionUnit\": \"none\", \"XResolution\": \"4\", \"YResolution\": \"3\", \"jpeg:subsampling\": \"4:2:0\", \"oiio:ColorSpace\": \"sRGB\"}"
                    }
                ],
                "intrinsics": [
                    {
                        "intrinsicId": 2798600110,
                        "pxInitialFocalLength": -1.0,
                        "pxFocalLength": 1738.2337649086282,
                        "type": "radial3",
                        "width": 1440,
                        "height": 1080,
                        "serialNumber": "D:/Documents/GitHub/bsc_kovinev/datasets/1440-1080-20",
                        "principalPoint": {
                            "x": 720.0,
                            "y": 540.0
                        },
                        "initializationMode": "unknown",
                        "distortionParams": [
                            0.0,
                            0.0,
                            0.0
                        ],
                        "locked": false
                    }
                ],
                "sensorDatabase": "C:\\Users\\Alien\\Desktop\\Meshroom-2019.2.0\\aliceVision\\share\\aliceVision\\cameraSensors.db",
                "defaultFieldOfView": 45.0,
                "groupCameraFallback": "folder",
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/cameraInit.sfm"
            }
        },
        "FeatureExtraction_1": {
            "nodeType": "FeatureExtraction",
            "position": [
                155,
                0
            ],
            "parallelization": {
                "blockSize": 40,
                "size": 50,
                "split": 2
            },
            "uids": {
                "0": "5f81e03c1f42aa1127ead623fdbe09e51d865f13"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{CameraInit_1.output}",
                "describerTypes": [
                    "sift"
                ],
                "describerPreset": "normal",
                "forceCpuExtraction": true,
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/"
            }
        },
        "ImageMatching_1": {
            "nodeType": "ImageMatching",
            "position": [
                310,
                0
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 50,
                "split": 1
            },
            "uids": {
                "0": "d4a833f1c39d50f04c825ebd0bcd758abd82eb93"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{FeatureExtraction_1.input}",
                "featuresFolders": [
                    "{FeatureExtraction_1.output}"
                ],
                "tree": "C:\\Users\\Alien\\Desktop\\Meshroom-2019.2.0\\aliceVision\\share\\aliceVision\\vlfeat_K80L3.SIFT.tree",
                "weights": "",
                "minNbImages": 200,
                "maxDescriptors": 500,
                "nbMatches": 50,
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/imageMatches.txt"
            }
        },
        "FeatureMatching_1": {
            "nodeType": "FeatureMatching",
            "position": [
                465,
                0
            ],
            "parallelization": {
                "blockSize": 20,
                "size": 50,
                "split": 3
            },
            "uids": {
                "0": "bd539dec901617a30bcf64958b628866ce38f3d3"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{ImageMatching_1.input}",
                "featuresFolders": "{ImageMatching_1.featuresFolders}",
                "imagePairsList": "{ImageMatching_1.output}",
                "describerTypes": [
                    "sift"
                ],
                "photometricMatchingMethod": "ANN_L2",
                "geometricEstimator": "acransac",
                "geometricFilterType": "fundamental_matrix",
                "distanceRatio": 0.8,
                "maxIteration": 2048,
                "geometricError": 0.0,
                "maxMatches": 0,
                "savePutativeMatches": false,
                "guidedMatching": false,
                "exportDebugFiles": false,
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/"
            }
        },
        "StructureFromMotion_1": {
            "nodeType": "StructureFromMotion",
            "position": [
                620,
                0
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 50,
                "split": 1
            },
            "uids": {
                "0": "429da1ad7bec1171ecbb880898f48a669c50d935"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{FeatureMatching_1.input}",
                "featuresFolders": "{FeatureMatching_1.featuresFolders}",
                "matchesFolders": [
                    "{FeatureMatching_1.output}"
                ],
                "describerTypes": [
                    "sift"
                ],
                "localizerEstimator": "acransac",
                "localizerEstimatorMaxIterations": 4096,
                "localizerEstimatorError": 0.0,
                "lockScenePreviouslyReconstructed": false,
                "useLocalBA": true,
                "localBAGraphDistance": 1,
                "maxNumberOfMatches": 0,
                "minInputTrackLength": 2,
                "minNumberOfObservationsForTriangulation": 2,
                "minAngleForTriangulation": 3.0,
                "minAngleForLandmark": 2.0,
                "maxReprojectionError": 4.0,
                "minAngleInitialPair": 5.0,
                "maxAngleInitialPair": 40.0,
                "useOnlyMatchesFromInputFolder": false,
                "useRigConstraint": true,
                "lockAllIntrinsics": false,
                "initialPairA": "",
                "initialPairB": "",
                "interFileExtension": ".abc",
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/sfm.abc",
                "outputViewsAndPoses": "{cache}/{nodeType}/{uid0}/cameras.sfm",
                "extraInfoFolder": "{cache}/{nodeType}/{uid0}/"
            }
        },
        "PrepareDenseScene_1": {
            "nodeType": "PrepareDenseScene",
            "position": [
                775,
                0
            ],
            "parallelization": {
                "blockSize": 40,
                "size": 50,
                "split": 2
            },
            "uids": {
                "0": "ebf6bdd20d18d8b677a1a7b48810143838c6124f"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{StructureFromMotion_1.output}",
                "imagesFolders": [],
                "outputFileType": "exr",
                "saveMetadata": true,
                "saveMatricesTxtFiles": false,
                "evCorrection": false,
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/",
                "outputUndistorted": "{cache}/{nodeType}/{uid0}/*.{outputFileTypeValue}"
            }
        },
        "DepthMap_1": {
            "nodeType": "DepthMap",
            "position": [
                930,
                0
            ],
            "parallelization": {
                "blockSize": 3,
                "size": 50,
                "split": 17
            },
            "uids": {
                "0": "dd77c088cc8ce145d16d694d756db7b0ac5eb39a"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{PrepareDenseScene_1.input}",
                "imagesFolder": "{PrepareDenseScene_1.output}",
                "downscale": 2,
                "minViewAngle": 2.0,
                "maxViewAngle": 70.0,
                "sgmMaxTCams": 10,
                "sgmWSH": 4,
                "sgmGammaC": 5.5,
                "sgmGammaP": 8.0,
                "refineMaxTCams": 6,
                "refineNSamplesHalf": 150,
                "refineNDepthsToRefine": 31,
                "refineNiters": 100,
                "refineWSH": 3,
                "refineSigma": 15,
                "refineGammaC": 15.5,
                "refineGammaP": 8.0,
                "refineUseTcOrRcPixSize": false,
                "exportIntermediateResults": false,
                "nbGPUs": 0,
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/"
            }
        },
        "DepthMapFilter_1": {
            "nodeType": "DepthMapFilter",
            "position": [
                1085,
                0
            ],
            "parallelization": {
                "blockSize": 10,
                "size": 50,
                "split": 5
            },
            "uids": {
                "0": "1b11cdbbc6e0ff35c00ef82c78471ddd4831dfdf"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{DepthMap_1.input}",
                "depthMapsFolder": "{DepthMap_1.output}",
                "minViewAngle": 2.0,
                "maxViewAngle": 70.0,
                "nNearestCams": 10,
                "minNumOfConsistentCams": 3,
                "minNumOfConsistentCamsWithLowSimilarity": 4,
                "pixSizeBall": 0,
                "pixSizeBallWithLowSimilarity": 0,
                "computeNormalMaps": false,
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/"
            }
        },
        "Meshing_1": {
            "nodeType": "Meshing",
            "position": [
                1240,
                0
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "140f9ceb33e46c75ccfc580a4e22059fbfbaeab4"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{DepthMapFilter_1.input}",
                "depthMapsFolder": "{DepthMapFilter_1.depthMapsFolder}",
                "depthMapsFilterFolder": "{DepthMapFilter_1.output}",
                "estimateSpaceFromSfM": true,
                "estimateSpaceMinObservations": 3,
                "estimateSpaceMinObservationAngle": 10,
                "maxInputPoints": 50000000,
                "maxPoints": 5000000,
                "maxPointsPerVoxel": 1000000,
                "minStep": 2,
                "partitioning": "singleBlock",
                "repartition": "multiResolution",
                "angleFactor": 15.0,
                "simFactor": 15.0,
                "pixSizeMarginInitCoef": 2.0,
                "pixSizeMarginFinalCoef": 4.0,
                "voteMarginFactor": 4.0,
                "contributeMarginFactor": 2.0,
                "simGaussianSizeInit": 10.0,
                "simGaussianSize": 10.0,
                "minAngleThreshold": 1.0,
                "refineFuse": true,
                "addLandmarksToTheDensePointCloud": false,
                "colorizeOutput": false,
                "saveRawDensePointCloud": false,
                "verboseLevel": "info"
            },
            "outputs": {
                "outputMesh": "{cache}/{nodeType}/{uid0}/mesh.obj",
                "output": "{cache}/{nodeType}/{uid0}/densePointCloud.abc"
            }
        },
        "MeshFiltering_1": {
            "nodeType": "MeshFiltering",
            "position": [
                1395,
                0
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "4e3ec035891d697af16f94bf7ad6264d5b14b33a"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "inputMesh": "{Meshing_1.outputMesh}",
                "removeLargeTrianglesFactor": 60.0,
                "keepLargestMeshOnly": false,
                "iterations": 5,
                "lambda": 1.0,
                "verboseLevel": "info"
            },
            "outputs": {
                "outputMesh": "{cache}/{nodeType}/{uid0}/mesh.obj"
            }
        },
        "Texturing_1": {
            "nodeType": "Texturing",
            "position": [
                1550,
                0
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "9be6da826f959a6080584fe5180972565033a75d"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{Meshing_1.output}",
                "imagesFolder": "{DepthMap_1.imagesFolder}",
                "inputMesh": "{MeshFiltering_1.outputMesh}",
                "textureSide": 8192,
                "downscale": 1,
                "outputTextureFileType": "png",
                "unwrapMethod": "Basic",
                "useUDIM": true,
                "fillHoles": false,
                "padding": 5,
                "correctEV": false,
                "useScore": true,
                "processColorspace": "sRGB",
                "multiBandDownscale": 4,
                "multiBandNbContrib": {
                    "high": 1,
                    "midHigh": 5,
                    "midLow": 10,
                    "low": 0
                },
                "bestScoreThreshold": 0.1,
                "angleHardThreshold": 90.0,
                "forceVisibleByAllVertices": false,
                "flipNormals": false,
                "visibilityRemappingMethod": "PullPush",
                "verboseLevel": "info"
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/",
                "outputMesh": "{cache}/{nodeType}/{uid0}/texturedMesh.obj",
                "outputMaterial": "{cache}/{nodeType}/{uid0}/texturedMesh.mtl",
                "outputTextures": "{cache}/{nodeType}/{uid0}/texture_*.{outputTextureFileTypeValue}"
            }
        }
    }
}