from flask import Flask, request, render_template
import math
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 20080

@app.route('/', methods=['GET'])
def get_html():
    return render_template('./test.html')


@app.route('/lux', methods=['POST'])
def update_lux():
    lux = request.form["lux"]
    try:
        f = open(file_path, 'a')
        f.write(lux + " ")
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/lux', methods=['GET'])
def get_lux():
    split_lux = []
    float_lux = []

    try:
        f = open(file_path, 'r')
        for row in f:
            lux = row

        split_lux = lux.split()
        for item in split_lux:
            float_lux.append(float(item))

        mean = sum(float_lux)/len(float_lux)
        mean_adjust = round(mean,2)
        mean_adjust = str(mean_adjust)

    except Exception as e:
        print(e)
    finally:
        f.close()
        f = open(file_path, 'w')
        f.close()
        return mean_adjust
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_num)