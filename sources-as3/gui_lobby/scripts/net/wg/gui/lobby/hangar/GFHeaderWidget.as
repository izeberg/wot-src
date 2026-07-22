package net.wg.gui.lobby.hangar
{
   import flash.events.Event;
   import net.wg.data.constants.generated.HANGAR_ALIASES;
   import net.wg.gui.lobby.hangar.quests.HeaderQuestsFlags;
   import net.wg.infrastructure.base.meta.IGFHeaderWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.GFHeaderWidgetMeta;
   
   public class GFHeaderWidget extends GFHeaderWidgetMeta implements IGFHeaderWidgetMeta
   {
       
      
      private var _marginTop:int = 0;
      
      private var _marginRight:int = 0;
      
      private var _marginLeft:int = 0;
      
      public function GFHeaderWidget()
      {
         super();
         setManageSize(false);
         alias = HANGAR_ALIASES.GF_HEADER_WIDGET;
         addEventListener(Event.RESIZE,this.onProxyResize);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(Event.RESIZE,this.onProxyResize);
         super.onDispose();
      }
      
      public function as_updateMargins(param1:int, param2:int, param3:int) : void
      {
         this._marginTop = param1;
         this._marginRight = param2;
         this._marginLeft = param3;
         dispatchEvent(new Event(HeaderQuestsFlags.ENTRY_POINT_RESIZE));
      }
      
      override public function get marginTop() : int
      {
         return this._marginTop;
      }
      
      override public function get marginRight() : int
      {
         return this._marginRight;
      }
      
      override public function get marginLeft() : int
      {
         return this._marginLeft;
      }
      
      private function onProxyResize(param1:Event) : void
      {
         getProxyUnsafe().x = -width >> 1;
      }
   }
}
