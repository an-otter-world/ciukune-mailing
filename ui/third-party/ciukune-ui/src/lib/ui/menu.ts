import { Component } from 'vue'
import { CiukuneApp } from '../../main'

export interface MenuItemDescriptor {
  component: Component,
  icon: string
  label: string,
  path: string,
}

export interface MenuItem {
  path: string,
  icon: string
}

export class Menu {
  constructor(parentRoute: string | undefined = undefined){
    this._parentRoute = parentRoute
  }

  *items() {
    for(const item of this._items) {
      yield {
        label: item.label,
        icon: item.icon,
        link: this._parentRoute + '/' + item.path
      }
    } 
  }  

  addItem(item: MenuItemDescriptor) {
    if(this._parentRoute) {
      CiukuneApp.$router.addRoute(this._parentRoute, {
        path: item.path,
        component: item.component
      })
    }
    else {
      CiukuneApp.$router.addRoute({
        path: item.path,
        component: item.component
      })

    }
  }

  private readonly _parentRoute: string | undefined
  private readonly _items: MenuItemDescriptor[] = []
}
