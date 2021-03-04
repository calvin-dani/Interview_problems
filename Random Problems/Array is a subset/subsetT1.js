function isSubset(array1,array2){

    if(array1.length > array2.length){
        temp = array1;
        array1 = array2;
        array2 = temp;
    }

    if(array1.length == 0){
        return true;
    }

    arrDic = new Set(array2);

    return array1.reduce((acc,curr)=>{
        if(acc == false){
            return false;
        }
        if(!arrDic.has(curr)){
            return false;
        }
        return true
    },true);
}

console.log(isSubset([1, 2], [3, 5, 9, 1]));