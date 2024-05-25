import { Routes } from '@angular/router';
import { PlayeruiComponent } from './playerui/playerui.component';
import { SideBarComponent } from './side-bar/side-bar.component';
import { LayoutComponent } from './layout/layout.component';
import { TeamGenerationComponent } from './team-generation/team-generation.component';

export const routes: Routes = [
    {
        path: '',
        component: LayoutComponent,
        children: [
          { path: 'player-info', component: PlayeruiComponent },
          { path: 'team-generation', component: TeamGenerationComponent },
          { path: '', redirectTo: 'player-info', pathMatch: 'full' }
        ]
      },
    ///{path:'',component:SideBarComponent}
];
