import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AutorithationComponent } from './Components/autorithation/autorithation.component';
import { MainPageComponent } from './Components/main-page/main-page.component';
import { ChatBotComponent } from './Components/chat-bot/chat-bot.component';

const routes: Routes = [

  {path: 'sign-in', component:AutorithationComponent},
  {path: '', component:MainPageComponent},
  {path: 'chat-bot', component:ChatBotComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
