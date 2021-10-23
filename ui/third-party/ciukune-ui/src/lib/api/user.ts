import { getApi, ObjectResource } from '@dontnod/wlh'

export class User extends ObjectResource {
  static EMAIL = 'email'
  get email() { return this.get<string>(User.EMAIL) }
  set email(value: string) { this.set<string>(User.EMAIL, value) }

  static USERNAME = 'username'
  get username() { return this.get<string>(User.USERNAME) }
  set username(value: string) { this.set<string>(User.USERNAME, value) }
}
