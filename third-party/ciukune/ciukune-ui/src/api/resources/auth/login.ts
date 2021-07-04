import { Backend, Resource } from '@ciukune/ckc'
import { getResource } from '@ciukune/ckc'
import { getMeResource } from '../user/me'
import { MeResource } from '../user/me'

interface LoginResponse {
  access: string
  refresh: string
}

export class LoginResource extends Resource {
  email: string | undefined
  password: string | undefined

  constructor(url: string, backend: Backend) {
    super(url, backend)
    this._me = getMeResource()
  }

  async login() {
    let response = await this._post<LoginResponse, {}>({
      email: this.email,
      password: this.password
    })

    if(!response) {
      return;
    }

    this.email = undefined
    this.password = undefined

    this.backend.setToken(response.access)
    await this._me.load()
  }
  
  async logout() {
    this.backend.clearToken()
    await this._me.load()
  }

  private _me: MeResource
}

export function getLoginResource() {
  return getResource(LoginResource, 'auth/login')
}
