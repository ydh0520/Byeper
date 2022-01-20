# :classical_building: Byper - Bye Paper

## :bulb: IN THE Byper

온라인 강의를 위한 동영상 압축 서비스 입니다.

Youtube 동영상 강의를 PPT와 같은 문서 자로료 변환시켜 드립니다.

원하는 강의(동영상)의 재생목록을 만들고 수강 진행도를 확인할수 있습니다.

강사지원을 통해 자신의 강의를 업로드 할 수 있습니다.

# :tada: Getting Started

## Front end
```
cd ./frontend
npm install
npm run serve or npm run build
```
## Back end(Spring)
```
cd ./backend/Spring
mvn package
java -jar target/Teletubbies-0.0.1-SNAPSHOT.jar
```

## Back end(Django)
```
cd backend/Django
pip install -r requirements.txt
python manage.py runserver
```

# :wrench: Configuration

## require
- [Mavne](https://maven.apache.org/)
- [Node.js](https://nodejs.org/en/)
- [Mysql](https://www.mysql.com/)
- [Redis](https://redis.io/)
- [Google login](https://developers.google.com/identity/sign-in/web)
- [JWT](https://jwt.io/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Frontend Config
### BaseUrl Config ( ./frontend/src/service/axios.service.ts )
```
...
export class Axios {
  static readonly instance: AxiosInstance = axios.create({
    baseURL: `Your_base_url`,
    timeout: 10000
  });
}
...
```

### Google Login Config ( ./frontend/src/main.ts )
```
...
Vue.use(GAuth, {
  clientId: `Google_Client_ID`,
  scope: "profile email https://www.googleapis.com/auth/plus.login",
});
...
```
## Backend Config

### DB Config ( ./backend/Spring/src/main/resources/application.properties )
```
# MySql
spring.datasource.driverClassName=com.mysql.cj.jdbc.Driver
spring.datasource.url=  `mysql_url`
spring.datasource.username= `mysql_user_name`
spring.datasource.password= `mysql_user_password`

#Redis
spring.cache.type=redis
spring.redis.host= `redis_url`
spring.redis.port= `redis_port`

```


### Google Login Config( ./backend/Spring/src/main/java/com/ssafy/config/GoogleLoginConfig.java )
```
public static final String GOOGLE_CLIENT_ID = `Google_Client_ID`;
public static final String GOOGLE_SECRIT_ID = `Google_Secrit_ID`;
...
	@Bean
OAuth2Parameters oAuth2Parameters() {
	OAuth2Parameters oAuth2Parameters = new OAuth2Parameters();
	oAuth2Parameters.setRedirectUri( `Redirect_url` );
	oAuth2Parameters.setScope( `Google_Login_scope` );
	return oAuth2Parameters;
}

```
### JWT Config ( ./backend/Springsrc/main/java/com/ssafy/config/JwtProperties.java )
```
public class JwtProperties {
    ...
    public static final String SECRET = `Your_JWT_Secrit_Key`;
    ...
}
```

## :pencil: Tech Stack

### Front end
- Vue
- Vuex
- Vue-Router
- TypeScript
- Eslint
- Prettier
- vue-google-oauth2
- axios

### Back end

- Spring Boot
- Spring Security
- Django
- Django REST framework
- Pandas
- TensorFlow
- JWT
- Swagger

### DB

- Mysql
- Redis

### CI/CD

- Jenkins
- Docker
- nginx



## :busts_in_silhouette: Author

- 이연재 - FE
- 김동욱 - FE
- 김태인 - FE
- 편재호 - FE
- 김원호 - 동영상 
- 윤동현 - BE



