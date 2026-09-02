package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.hangar.data.LobbyVisibilityVO;
   import net.wg.infrastructure.base.AbstractView;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class LobbyPageMeta extends AbstractView
   {
       
      
      public var moveSpace:Function;
      
      public var getSubContainerTypes:Function;
      
      public var notifyCursorOver3dScene:Function;
      
      public var notifyCursorDragging:Function;
      
      private var _lobbyVisibilityVO:LobbyVisibilityVO;
      
      public function LobbyPageMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._lobbyVisibilityVO)
         {
            this._lobbyVisibilityVO.dispose();
            this._lobbyVisibilityVO = null;
         }
         super.onDispose();
      }
      
      public function moveSpaceS(param1:Number, param2:Number, param3:Number) : void
      {
         App.utils.asserter.assertNotNull(this.moveSpace,"moveSpace" + Errors.CANT_NULL);
         this.moveSpace(param1,param2,param3);
      }
      
      public function getSubContainerTypesS() : Array
      {
         App.utils.asserter.assertNotNull(this.getSubContainerTypes,"getSubContainerTypes" + Errors.CANT_NULL);
         return this.getSubContainerTypes();
      }
      
      public function notifyCursorOver3dSceneS(param1:Boolean) : void
      {
         App.utils.asserter.assertNotNull(this.notifyCursorOver3dScene,"notifyCursorOver3dScene" + Errors.CANT_NULL);
         this.notifyCursorOver3dScene(param1);
      }
      
      public function notifyCursorDraggingS(param1:Boolean) : void
      {
         App.utils.asserter.assertNotNull(this.notifyCursorDragging,"notifyCursorDragging" + Errors.CANT_NULL);
         this.notifyCursorDragging(param1);
      }
      
      public final function as_setInterfaceVisible(param1:Object) : void
      {
         var _loc2_:LobbyVisibilityVO = this._lobbyVisibilityVO;
         this._lobbyVisibilityVO = new LobbyVisibilityVO(param1);
         this.setInterfaceVisible(this._lobbyVisibilityVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setInterfaceVisible(param1:LobbyVisibilityVO) : void
      {
         var _loc2_:String = "as_setInterfaceVisible" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
