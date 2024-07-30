
// var 함수 스코프. 중복 선언 가능. 
// let 블록 스코프. 중복 선언 불가능. 
// ; 생략 가능하다

num = 5; // var 생략 가능
console.log(typeof(num));
// 자료형 undefind, number(NaN), string, boolean, object(null), function, 

// + 연산자 일때 자동 형변환 한다.
console.log('hi' + 10); // 'hi10'
console.log(10 + true); // 11
console.log(Number('hi')); // 에러가 안남. NaN
console.log(typeof(null)); // object

// === 값과 타입까지 같은지 검사하는 비교연산자
console.log(`1 == '1' : ${1 == '1'}`) // true
console.log(`1 === '1' : ${1 === '1'}`) // false

// 상수 constant
const one = 1
// one = 2 상수 선언 후에 값을 변경 할 수 없음

array = [1,2,3,4,5]
for (let index = 0; index < array.length; index++) {
    const element = array[index];
    console.log(element + 'for')
}

array.forEach(element => {
    console.log(element + 'forEach')
});

// 배열이나 리스트
for (const iterator of object=[1,2,3,4,5]) {
    // 제어문 
    if(iterator % 2 == 0){
        console.log(iterator + '짝')
    }else if(iterator % 2 != 0){
        console.log(iterator + '홀')
    }else{
        console.log('else')
    }
    
}

// 배열 외의 것
for (const key in object={'name': 'cho', 'age':42}) {
    if (Object.hasOwnProperty.call(object, key)) {
        const element = object[key];
        console.log(element)
    }
}

