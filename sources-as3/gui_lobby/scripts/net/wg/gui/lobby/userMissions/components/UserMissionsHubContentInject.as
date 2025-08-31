package net.wg.gui.lobby.userMissions.components
{
   import net.wg.infrastructure.base.meta.IUserMissionsHubContentInjectMeta;
   import net.wg.infrastructure.base.meta.impl.UserMissionsHubContentInjectMeta;
   
   public class UserMissionsHubContentInject extends UserMissionsHubContentInjectMeta implements IUserMissionsHubContentInjectMeta
   {
       
      
      public function UserMissionsHubContentInject()
      {
         super();
         setManageSize(true);
      }
   }
}
