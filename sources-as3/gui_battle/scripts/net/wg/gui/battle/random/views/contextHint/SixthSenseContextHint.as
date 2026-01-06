package net.wg.gui.battle.random.views.contextHint
{
   import net.wg.infrastructure.base.meta.ISixthSenseContextHintMeta;
   import net.wg.infrastructure.base.meta.impl.SixthSenseContextHintMeta;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   import scaleform.clik.constants.InvalidationType;
   
   public class SixthSenseContextHint extends SixthSenseContextHintMeta implements ISixthSenseContextHintMeta, IDisplayableComponent
   {
      
      private static const WIDTH:uint = 1609;
      
      private static const HEIGHT:uint = 905;
       
      
      private var _isCompVisible:Boolean = false;
      
      private var _isVisible:Boolean = false;
      
      public function SixthSenseContextHint()
      {
         super();
         setManageSize(true);
         mouseEnabled = mouseChildren = false;
         width = WIDTH;
         height = HEIGHT;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(visible != (this._isCompVisible && this._isVisible) && isInvalid(InvalidationType.STATE))
         {
            visible = this._isCompVisible && this._isVisible;
         }
      }
      
      public function as_setVisibility(param1:Boolean) : void
      {
         if(this._isVisible != param1)
         {
            this._isVisible = param1;
            invalidateState();
         }
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         if(this._isCompVisible != param1)
         {
            this._isCompVisible = param1;
            invalidateState();
         }
      }
      
      public function updatePosition(param1:int, param2:int) : void
      {
         x = param1 - (WIDTH >> 1);
         y = param2 - (HEIGHT >> 1);
      }
   }
}
