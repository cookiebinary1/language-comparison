fn main(){
    let mut i:i64 = 0;
    let mut x:i64 = 0;

    while i < 100000000 {
        x += i;
        i += 1;
    }
    println!("Result is: {}", x);
}