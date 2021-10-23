import { getApi, ObjectResource } from '@dontnod/wlh'

export class Login extends ObjectResource {
  email: string | undefined
  password: string | undefined

  async login() {
    let response = await this._post({
      email: this.email,
      password: this.password
    }) as {
      access: string
    }

    if(!response) {
      return;
    }

    this.email = undefined
    this.password = undefined

    this.api.setToken(response.access)
  }
  
  async logout() {
    this.api.clearToken()
    await this.load(true)
  }
}

export function getLogin() {
  return getApi().get(Login, 'auth/login')
}
