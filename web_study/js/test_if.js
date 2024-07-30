// if 문

let num = [10, 20, 30, 40, 50, 60, 70, 80, 90];

for (const i of num) {
    if ( i >= 90){
        console.log(`${i} 는 A`)
    }else if ( i >= 80){
        console.log(`${i} 는 B`)
    }else{
        console.log(`${i} 는 C`)
    }
}

let menu = [1, 2, 3, 4]

for (const i of menu) {
    switch (i) {
        case 1:
            console.log('짜장')
            break;
        case 2:
            console.log('짬뽕')
            break;
        case 3:
            console.log('뽁음')
            break;
        case 4:
            console.log('탕슉')
            break;
        default:
            break;
    }    
}

let order = 1
switch (order) {
    case 1:
        console.log('입금')
        break;
    case 2:
        console.log('출금')
        break;
    case 3:
        console.log('잔액 조회')
        break;
    case 4:
        console.log('안녕히 가세요')
        break;
    default:
        break;
}


const repl = require('repl');

// REPL 서버 시작
const server = repl.start({
    prompt: 'my-repl> ',
    eval: (cmd, context, filename, callback) => {
        let result;
        try {
            result = eval(cmd);
        } catch (e) {
            result = e;
        }
        callback(null, result);
    }
});

// REPL 환경에 변수 추가
server.context.myVariable = 42;
