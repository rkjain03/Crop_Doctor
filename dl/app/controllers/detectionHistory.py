from app.controllers import blueprint,mongo,jsonify,datetime,resnet,request
from app.schemas import validate_detectionHistory
from bson.objectid import ObjectId

@blueprint.route('/api/dl',methods=["GET"])
def hello():
    return 'Hello, World!'

@blueprint.route('/api/dl/prediction/test',methods=['GET'])
def test1():
    print(ObjectId("623a3d74960a9f8526395e08"))
    data = validate_detectionHistory({"createdAt":str(datetime.now()),"plantId":ObjectId("623a3d74960a9f8526395e08")})
    if data['ok']:
        data = data['data']
        print(mongo.db.detectionHistory.find_one())
        print(type(mongo.db.detectionHistory.find_one()['_id']))
        mongo.db.detectionHistory.insert_one(data)
        return jsonify({'ok': True, 'message': 'User created successfully!','detectionHistory':data}), 200
    
    return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

@blueprint.route('/api/dl/detection',methods=['POST'])
def dl_detection():
    try:
        uid = request.headers['uid']
        city = request.headers['city']
        ip = request.headers['ip']
        district = request.headers['district']
        state = request.headers['state']
        lat = request.form['lat'] if("lat" in request.form) else request.headers['lat']
        lon = request.form['lon'] if("lon" in request.form) else request.headers['lon']

        image =request.files['image']
        detection = resnet.predict_image(image)
        detection_split = detection.split('___')
        plant,disease = detection_split[0],detection_split[1]

        disease_info = mongo.db.disease.find_one({"name": detection})
        plant_info = mongo.db.plants.find_one({"commonName":plant})
        print(disease_info,plant_info,plant)

        detectionHistory = {
        "createdAt": str(datetime.now()),
        "ip": ip,
        "city":city,
        "district":district,
        "state":state,
        "location": {
            "lat":lat,
            "lon":lon
        },
        "detected_class":detection,
        "plantId":ObjectId("623a3d74960a9f8526395e08"),
        "diseaseId":ObjectId("623a3d74960a9f8526395e08"),
        "rating":5
        }

        validated_detectionHistory = validate_detectionHistory(detectionHistory)
        done = mongo.db.detectionHistory.insert_one(validated_detectionHistory )

        return jsonify({'ok': True, 'detection': detection,'validated_detectionHistory ':validated_detectionHistory},"plant":plant_info,"disease":"No disease found" if disease_info==None else disease_info}), 200
    except Exception as ex:
        return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(ex)}), 400

    # print(ObjectId("623a3d74960a9f8526395e08"))
    # data = validate_detectionHistory({"createdAt":str(datetime.now()),"plantId":ObjectId("623a3d74960a9f8526395e08")})
    # if data['ok']:
    #     data = data['data']
    #     print(mongo.db.detectionHistory.find_one())
    #     print(type(mongo.db.detectionHistory.find_one()['_id']))
    #     mongo.db.detectionHistory.insert_one(data)
    #     return jsonify({'ok': True, 'message': 'User created successfully!','detectionHistory':data}), 200
    

