let sum = 0;
// 기본적인 형태
for (let i = 0; i <= 10; i++) { 
    sum += i;
}
console.log(sum)
// 55

// 열거자의 인덱스를 받음
for (i in 'abcde'){
    console.log(i);
}
// 0 1 2 3 4

// 열거자의 값을 받음
for (i of 'abcde'){
    console.log(i);
}
// a b c d e

// 배열의 내장 함수
arr = [1,2,3,4,5];

console.log(arr.length)

arr.forEach(i => {
    console.log(i);
});
// 1 2 3 4 5 

// 조건형 반복문
sum = 5;
while (sum > 0) {
    console.log(sum--);
}
// 5 4 3 2 1

console.log('end')
sum = 5;
// 초기식 조건식 증감식 생략가능
for (;;){
    //console.log(sum--);
    process.stdout.write(String(sum--));
    if(sum <= 0){
        break;
    }
}
// 5 4 3 2 1

lambda = (x) => { return x; } //  화살표 함수(arrow function) 콜백함수 쓸때 간략하게 쓸려고 만듦.
lambda = x =>  x //  화살표 함수(arrow function) 괄호, return 키워드 생략 가능
console.log(lambda('hi'))


