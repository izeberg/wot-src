package net.wg.gui.battle.views.decorativeCrosshair
{
   import net.wg.infrastructure.base.meta.IBaseDecorativeCrosshairMeta;
   import net.wg.infrastructure.base.meta.impl.BaseDecorativeCrosshairMeta;
   
   public class BaseDecorativeCrosshair extends BaseDecorativeCrosshairMeta implements IBaseDecorativeCrosshairMeta
   {
      
      protected static const INSTANTLY_POSTFIX:String = "_instantly";
       
      
      protected var _state:String = "hide";
      
      public function BaseDecorativeCrosshair()
      {
         super();
      }
      
      public function as_setState(param1:String, param2:Boolean) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         if(param2 || !visible)
         {
            param1 += INSTANTLY_POSTFIX;
         }
         gotoAndPlay(param1);
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         setCompVisible(param1);
      }
      
      public function updateScale(param1:int) : void
      {
      }
      
      protected function setScale(param1:Number) : void
      {
         this.scaleX = this.scaleY = param1;
      }
   }
}
