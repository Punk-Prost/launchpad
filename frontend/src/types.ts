export type Stage='idea'|'prototype'|'mvp'|'growth';
export type Startup={id:number;name:string;slug:string;tagline:string;description:string;industry:string;stage:Stage;location:string;funding_goal:number;team_size:number;progress:number;is_featured:boolean;open_roles:string[];owner_id:number};
export type User={id:number;name:string;email:string;role:'founder'|'member'|'mentor'|'admin'};
