package net.wg.gui.lobby.components
{
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import net.wg.infrastructure.interfaces.IViewStackContent;
   
   public class ResizableViewStack extends DataViewStack
   {
      
      private static const OFFSET_INVALID:String = "layoutInv";
      
      private static const AVAILABLE_SIZE_INV:String = "availSizeInv";
       
      
      protected var paddings:Rectangle;
      
      private var _availableSize:Point = null;
      
      private var _centerOffset:int = 0;
      
      public function ResizableViewStack()
      {
         this.paddings = new Rectangle();
         super();
      }
      
      override public function show(param1:String, param2:String) : IViewStackContent
      {
         var _loc3_:IResizableContent = IResizableContent(currentView);
         var _loc4_:IViewStackContent = super.show(param1,param2);
         if(_loc3_)
         {
            _loc3_.active = false;
         }
         _loc3_ = IResizableContent(_loc4_);
         _loc3_.active = true;
         if(this._availableSize)
         {
            _loc3_.setViewSize(this._availableSize.x,this._availableSize.y,this.paddings);
         }
         _loc3_.centerOffset = this._centerOffset;
         return _loc4_;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(AVAILABLE_SIZE_INV))
         {
            if(this._availableSize && currentView)
            {
               IResizableContent(currentView).setViewSize(this._availableSize.x,this._availableSize.y,this.paddings);
            }
         }
         if(isInvalid(OFFSET_INVALID))
         {
            if(currentView)
            {
               IResizableContent(currentView).centerOffset = this._centerOffset;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this._availableSize = null;
         this.paddings = null;
         super.onDispose();
      }
      
      public function setAvailableSize(param1:Number, param2:Number, param3:Rectangle = null) : void
      {
         if(this._availableSize == null)
         {
            this._availableSize = new Point();
         }
         if(param3 == null)
         {
            param3 = new Rectangle();
         }
         this._availableSize.x = param1;
         this._availableSize.y = param2;
         this.paddings = param3;
         invalidate(AVAILABLE_SIZE_INV);
      }
      
      override public function get width() : Number
      {
         return Boolean(this._availableSize) ? Number(this._availableSize.x) : Number(super.width);
      }
      
      override public function get height() : Number
      {
         return Boolean(this._availableSize) ? Number(this._availableSize.y) : Number(super.height);
      }
      
      public function set centerOffset(param1:int) : void
      {
         this._centerOffset = param1;
         invalidate(OFFSET_INVALID);
      }
   }
}
