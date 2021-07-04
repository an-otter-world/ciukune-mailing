import { ResourceObject } from '@ciukune/ckc'
import { getResource } from '@ciukune/ckc'
import { User } from '../../types/user'

export class MeResource extends ResourceObject<User> {
}

export function getMeResource() : MeResource {
  return getResource(MeResource, 'user/me')
}
