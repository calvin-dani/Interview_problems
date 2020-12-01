function waterTrap(paramArr) {

    let startFlag = 0;
    let waterArea = 0;

    /* -----------------------------To check the starting point of collection ----------------------------*/
    let idx = 0;
    while (startFlag == 0) {
        let currentH = paramArr[idx];
        let nextH = paramArr[idx + 1];
        if (currentH > nextH) {
            startFlag = 1;
            break;
        }
        idx += 1;
    }
    /* -------------------------------End of finding the last point ----------------------------------------*/

    /* ----------------------------Initializing variables for the area algo---------------------------------*/
    tempIdx = idx;


    let referenceIdx = tempIdx;
    let areaToDelete = 0;

    /* ----------------End of initializing variables for the area algo-------------------------------------*/


    /*  ----------------------------------Algo begins------------------------------------
        Searching for the next big bar or the last bar
        multiplying the area between them and subtracting the space taken by the smaller bar inbetween them*/

    for (let idx = tempIdx + 1; idx < paramArr.length; idx++) {

        let currentH = paramArr[idx];
        let nextH = paramArr[idx + 1];

        if (paramArr[referenceIdx] <= currentH) {
            valueSelected = currentH > paramArr[referenceIdx] ? paramArr[referenceIdx] : currentH;
            waterArea += (idx - referenceIdx - 1) * valueSelected + areaToDelete;
            referenceIdx = idx;
            areaToDelete = 0;
            continue;
        }
        if (nextH == undefined) {
            valueSelected = currentH;
            waterArea += (idx - referenceIdx - 1) * valueSelected + areaToDelete;
            break;
        }
        areaToDelete -= currentH;
        console.log(waterArea,"waterarea");
    }

    /* -------------------------------------------End of algo---------------------------------------------- */

    return waterArea;
}







console.log(waterTrap([100, 1, 98, 2, 96, 3, 94, 4, 92, 5, 90]
    ));