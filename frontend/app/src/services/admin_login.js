import { http } from './config'

export default{
    login:(admin) => {
        return http.post('login/', admin)
    }
}