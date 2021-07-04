import { App } from 'vue'
import { Backend } from './backend'
import { InjectionKey } from 'vue'
import { Resource } from './resource'
import { getBackend } from './backend'
import { inject } from 'vue'
import { reactive } from 'vue'

type ResourceConstructor<TResource extends Resource> = { new(url: string, backend: Backend) : TResource }

class ResourceManager {

  get<TResource extends Resource>(backend: Backend, constructor: ResourceConstructor<TResource>, url: string) : TResource {
    if(url in this._resources) {
      let resourceRef = this._resources[url]
      let resource = resourceRef.deref()
      if(resource) {
        return resource as TResource
      }
    }

    let resource = reactive(new constructor(url, backend)) as TResource
    this._resources[url] = new WeakRef(resource)
    return resource
  }

  private _resources: Record<string, WeakRef<Resource>> = {}
}

const ResourceManagerKey : InjectionKey<ResourceManager> = Symbol()

export function getResource<TResource extends Resource>(constructor: ResourceConstructor<TResource>, url: string) {
  const backend = getBackend() 
  const manager = inject(ResourceManagerKey)
  if(!manager) {
    throw new Error("No resource manager available, please install it in Vue JS application through the resource-manager.ts/install method")
  }

  return manager.get(backend, constructor, url)
}

export function installResourceManager<T>(app: App<T>) {
  app.provide(ResourceManagerKey, new ResourceManager())
}
