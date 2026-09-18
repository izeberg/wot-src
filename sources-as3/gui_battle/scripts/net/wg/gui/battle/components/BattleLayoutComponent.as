package net.wg.gui.battle.components
{
   import flash.geom.Rectangle;
   import flash.geom.Transform;
   import net.wg.infrastructure.layoutPart.ILayoutPositionable;
   import net.wg.infrastructure.layoutPart.LayoutPartNodeEvent;
   
   public class BattleLayoutComponent extends BattleDisplayable implements ILayoutPositionable
   {
       
      
      public function BattleLayoutComponent()
      {
         super();
      }
      
      protected function updateLayoutProperties() : void
      {
         dispatchEvent(new LayoutPartNodeEvent(LayoutPartNodeEvent.PROPERTIES_UPDATED,name));
      }
      
      override public function set x(param1:Number) : void
      {
         if(super.x == param1)
         {
            return;
         }
         super.x = param1;
         this.updateLayoutProperties();
      }
      
      override public function set y(param1:Number) : void
      {
         if(super.y == param1)
         {
            return;
         }
         super.y = param1;
         this.updateLayoutProperties();
      }
      
      override public function set transform(param1:Transform) : void
      {
         if(super.transform == param1)
         {
            return;
         }
         super.transform = param1;
         this.updateLayoutProperties();
      }
      
      override public function set scaleY(param1:Number) : void
      {
         if(super.scaleY == param1)
         {
            return;
         }
         super.scaleY = param1;
         this.updateLayoutProperties();
      }
      
      override public function set scaleX(param1:Number) : void
      {
         if(super.scaleX == param1)
         {
            return;
         }
         super.scaleX = param1;
         this.updateLayoutProperties();
      }
      
      override public function set width(param1:Number) : void
      {
         if(super.width == param1)
         {
            return;
         }
         super.width = param1;
         this.updateLayoutProperties();
      }
      
      override public function set height(param1:Number) : void
      {
         if(super.height == param1)
         {
            return;
         }
         super.height = param1;
         this.updateLayoutProperties();
      }
      
      override public function set visible(param1:Boolean) : void
      {
         if(super.visible == param1)
         {
            return;
         }
         super.visible = param1;
         dispatchEvent(new LayoutPartNodeEvent(LayoutPartNodeEvent.VISIBILITY_CHANGED,name));
      }
      
      public function applyLayoutPosition(param1:Rectangle) : void
      {
      }
   }
}
