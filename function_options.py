from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import openai
import configparser
config = configparser.ConfigParser()
config.read('config.txt')
openai.api_key = config.get('openai_api_key', 'openai_api_key')

@app.route('/submit', methods=['POST'])
def submit():
    function_options = request.form.get('function_options')
    inputText = request.form.get('inputText')
    reply_text = ""

    if function_options == "@AI聊天":
        import chat
        reply_text = chat.chat(inputText)
    elif function_options == "@即時翻譯":
        import translate
        reply_text = translate.translate(inputText)
    elif function_options == "@即時股票資訊":
        reply_text = "即時股票資訊---功能停用"
    elif function_options == "@發票兌獎":
            import prizes
            reply_text = prizes.shownum() + "\n\n" + prizes.getnum(inputText)
    elif function_options == "@即時股票資訊":
        reply_text = "即時股票資訊---功能停用"
    elif function_options == "@查詢BMI或生肖星座":
        reply_text = "查詢BMI或生肖星座---功能停用"
    
    # 將回傳結果轉換為 JSON 格式
    response = {'function_options': function_options,
                'inputText': inputText,
                'reply_text': reply_text}
    print(response)
    return jsonify(response)

if __name__ == "__main__":
    app.run()