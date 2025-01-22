package net.wg.gui.lobby.messengerBar
{
   import flash.display.DisplayObject;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.infrastructure.base.meta.IButtonWithCounterMeta;
   import net.wg.infrastructure.base.meta.impl.ButtonWithCounterMeta;
   import net.wg.infrastructure.interfaces.IDisplayObject;
   import net.wg.infrastructure.interfaces.IPopOverCaller;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.utils.Padding;
   
   public class ButtonWithCounter extends ButtonWithCounterMeta implements IButtonWithCounterMeta, IPopOverCaller, IDisplayObject
   {
       
      
      public var button:UniversalBtn = null;
      
      private var _count:int = 0;
      
      private var _label:String = "";
      
      public function ButtonWithCounter()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         App.utils.universalBtnStyles.setStyle(this.button,UniversalBtnStylesConst.STYLE_HEAVY_CRYSTAL);
         this.button.useHtmlText = true;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.button.label = this._label + (this._count > 0 ? this._count.toString() : Values.EMPTY_STR);
         }
      }
      
      override protected function onDispose() : void
      {
         this.button.dispose();
         this.button = null;
         super.onDispose();
      }
      
      public function as_setCount(param1:Number) : void
      {
         this._count = param1;
         invalidateData();
      }
      
      public function getHitArea() : DisplayObject
      {
         return this.button;
      }
      
      public function getTargetButton() : DisplayObject
      {
         return this.button;
      }
      
      override public function set enabled(param1:Boolean) : void
      {
         this.button.enabled = param1;
         super.enabled = param1;
      }
      
      override public function set visible(param1:Boolean) : void
      {
         this.button.visible = param1;
         super.visible = param1;
      }
      
      public function set label(param1:String) : void
      {
         this._label = param1;
         invalidateData();
      }
      
      public function set tooltip(param1:String) : void
      {
         this.button.tooltip = param1;
      }
      
      public function set iconSource(param1:String) : void
      {
         this.button.iconSource = param1;
      }
      
      public function set soundId(param1:String) : void
      {
         this.button.soundType = param1;
      }
      
      public function set soundType(param1:String) : void
      {
         this.button.soundId = param1;
      }
      
      public function set disabledFillPadding(param1:Padding) : void
      {
         this.button.disabledFillPadding = param1;
      }
   }
}
