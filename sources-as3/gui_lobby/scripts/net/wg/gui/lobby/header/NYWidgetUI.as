package net.wg.gui.lobby.header
{
   import flash.display.DisplayObjectContainer;
   import flash.display.Sprite;
   import flash.events.Event;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.gui.lobby.menu.LobbyMenu;
   import net.wg.infrastructure.interfaces.IManagedContent;
   import scaleform.gfx.FocusManager;
   
   public class NYWidgetUI extends GFInjectComponent
   {
      
      private static const WIDTH:int = 520;
      
      private static const HEIGHT:int = 188;
       
      
      public function NYWidgetUI()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(Event.REMOVED,this.onWrapperRemoved);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(Event.REMOVED,this.onWrapperRemoved);
         super.onDispose();
      }
      
      private function findManagedContent() : IManagedContent
      {
         var _loc1_:DisplayObjectContainer = this;
         while(_loc1_)
         {
            if(!_loc1_ || _loc1_ == App.stage)
            {
               return null;
            }
            if(_loc1_ is IManagedContent)
            {
               return IManagedContent(_loc1_);
            }
            _loc1_ = _loc1_.parent;
         }
         return null;
      }
      
      private function onWrapperRemoved(param1:Event) : void
      {
         param1.stopImmediatePropagation();
         if(FocusManager.getModalClip() is LobbyMenu)
         {
            FocusManager.setModalClip(Sprite(this.findManagedContent()));
         }
      }
   }
}
