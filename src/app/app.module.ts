import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ReactiveFormsModule } from '@angular/forms';
import { MainPageComponent } from './Components/main-page/main-page.component';
import { AutorithationComponent } from './Components/autorithation/autorithation.component';
import { ChatBotComponent } from './Components/chat-bot/chat-bot.component';

@NgModule({
  declarations: [
    AppComponent,
    MainPageComponent,
    AutorithationComponent,
    ChatBotComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
