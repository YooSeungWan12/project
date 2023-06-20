
\

    # html 에서 생성한 ID "add_text" 의 버튼이 눌렸을 때 호출될 pys-onClick 인자로 설정된 함수 생성
    def function_add_text():
            # html ID "input_text"와 "output_text" 와 연결된 객체 생성
        input_text1 = Element("name").value
        input_text2 = Element("email").value
        input_text3 = Element("phone").value
        output_text = Element("message")
        

        console.log(f'text: {input_text1}')
        console.log(f'text: {input_text2}')
        console.log(f'text: {input_text3}')
        # output_text 객체의 text 값을 input_text의 값으로 지정
        output_text.element.innerText = input_text1 + input_text2
        # 함수가 실행된 후 input_text의 값을 초기화
        input_text1.clear()
