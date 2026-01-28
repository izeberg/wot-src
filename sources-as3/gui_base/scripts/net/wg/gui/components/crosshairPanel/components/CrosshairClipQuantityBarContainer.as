package net.wg.gui.components.crosshairPanel.components
{
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.generated.CROSSHAIR_CASSETTE_TYPES;
   
   public class CrosshairClipQuantityBarContainer extends ClipQuantityIndicator
   {
      
      private static const MEDIUM_LIMIT:int = 31;
      
      private static const HEAVY_LIMIT:int = 13;
      
      private static const HEAVY_MB_LIMIT:int = 19;
      
      private static const LIGHT_CLIP_QUANTITY_BAR_TOTAL_FRAMES:int = 100;
      
      private static const MEDIUM_CLIP_QUANTITY_BAR_TOTAL_FRAMES:int = 31;
      
      private static const HEAVY_CLIP_QUANTITY_BAR_TOTAL_FRAMES:int = 13;
      
      private static const HEAVY_CLIP_QUANTITY_BAR_MB_TOTAL_FRAMES:int = 19;
      
      public static const TYPE_LIGHT:String = "ClipQuantityBarLightUI";
      
      public static const TYPE_MEDIUM:String = "ClipQuantityBarMediumUI";
      
      public static const TYPE_HEAVY:String = "ClipQuantityBarHeavyUI";
      
      public static const TYPE_HEAVY_MB:String = "ClipQuantityBarHeavyMbUI";
      
      public static const TYPE_AUTO_GUN:String = "ClipQuantityBarAutogunUI";
      
      private static const CLIP_CAPACITY_VALIDATION:String = "clipCapacityInvalid";
      
      private static const CLIP_INFO_VALIDATION:String = "clipInfoInvalid";
      
      private static const CLIP_RELOADING_VALIDATION:String = "clipReloadingInvalid";
       
      
      public var isUseFrameAnimation:Boolean = true;
      
      private var _clipCapacity:Number = -1;
      
      private var _hasMultipleBarrel:Boolean = false;
      
      private var _hasAutogun:Boolean = false;
      
      private var _burst:Number = -1;
      
      private var _currBar:CrosshairClipQuantityBar = null;
      
      private var _quantityInClip:Number = -1;
      
      private var _clipState:String = "normal";
      
      private var _isReloaded:Boolean = false;
      
      private var _reloadingState:String = "";
      
      public function CrosshairClipQuantityBarContainer()
      {
         super();
      }
      
      override public function setReloadingState(param1:String) : void
      {
         this._reloadingState = param1;
         invalidate(CLIP_RELOADING_VALIDATION);
      }
      
      override public function setClipsParam(param1:Number, param2:Number, param3:int) : void
      {
         if(this._clipCapacity != param1 || this._burst != param2)
         {
            this._clipCapacity = param1;
            this._burst = param2;
            this._hasMultipleBarrel = CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_TYPES.indexOf(param3) != -1;
            this._hasAutogun = param3 == CROSSHAIR_CASSETTE_TYPES.AUTO_GUN_CASSETTE;
            invalidate(CLIP_CAPACITY_VALIDATION);
         }
      }
      
      override public function updateInfo(param1:Number, param2:String, param3:Boolean) : void
      {
         this._quantityInClip = param1;
         this._clipState = param2;
         this._isReloaded = param3;
         invalidate(CLIP_INFO_VALIDATION);
      }
      
      override protected function onDispose() : void
      {
         if(this._currBar)
         {
            this._currBar.dispose();
            this._currBar = null;
         }
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var viewType:String = null;
         var mode:String = null;
         var clipTotalFrames:int = 0;
         var metric:Number = NaN;
         var heavyClipQuantityBarTotalFrames:int = 0;
         var viewClass:Class = null;
         super.draw();
         if(isInvalid(CLIP_CAPACITY_VALIDATION))
         {
            if(this._currBar)
            {
               this._currBar.dispose();
               removeChild(this._currBar);
               this._currBar = null;
            }
            if(this._clipCapacity > 1 && this._burst != this._clipCapacity)
            {
               viewType = TYPE_LIGHT;
               mode = CrosshairClipQuantityBar.MODE_PERCENT;
               clipTotalFrames = LIGHT_CLIP_QUANTITY_BAR_TOTAL_FRAMES;
               metric = this._clipCapacity;
               if(this._burst > 1)
               {
                  metric = Math.ceil(this._clipCapacity / this._burst);
               }
               if(this._hasAutogun)
               {
                  viewType = TYPE_AUTO_GUN;
               }
               else if(metric < this._hasMultipleBarrel ? Boolean(HEAVY_MB_LIMIT) : Boolean(HEAVY_LIMIT))
               {
                  viewType = !!this._hasMultipleBarrel ? TYPE_HEAVY_MB : TYPE_HEAVY;
                  heavyClipQuantityBarTotalFrames = !!this._hasMultipleBarrel ? int(HEAVY_CLIP_QUANTITY_BAR_MB_TOTAL_FRAMES) : int(HEAVY_CLIP_QUANTITY_BAR_TOTAL_FRAMES);
                  if(this._burst > 1)
                  {
                     mode = CrosshairClipQuantityBar.MODE_QUEUE;
                     clipTotalFrames = Math.min(metric + 1,heavyClipQuantityBarTotalFrames);
                  }
                  else
                  {
                     mode = CrosshairClipQuantityBar.MODE_AMMO;
                     clipTotalFrames = Math.min(this._clipCapacity + 1,heavyClipQuantityBarTotalFrames);
                  }
               }
               else if(metric < MEDIUM_LIMIT)
               {
                  viewType = TYPE_MEDIUM;
                  clipTotalFrames = MEDIUM_CLIP_QUANTITY_BAR_TOTAL_FRAMES;
                  if(this._burst > 1)
                  {
                     mode = CrosshairClipQuantityBar.MODE_QUEUE;
                     clipTotalFrames = Math.min(metric + 1,MEDIUM_CLIP_QUANTITY_BAR_TOTAL_FRAMES);
                  }
                  else
                  {
                     mode = CrosshairClipQuantityBar.MODE_AMMO;
                     clipTotalFrames = Math.min(this._clipCapacity + 1,MEDIUM_CLIP_QUANTITY_BAR_TOTAL_FRAMES);
                  }
               }
               try
               {
                  viewClass = getDefinitionByName(viewType) as Class;
                  this._currBar = new viewClass();
                  this._currBar.initialize(mode,this._clipCapacity,this._burst,clipTotalFrames,this.isUseFrameAnimation);
                  addChild(this._currBar);
                  invalidate(CLIP_INFO_VALIDATION);
               }
               catch(error:Error)
               {
               }
            }
         }
         if(this._currBar)
         {
            if(isInvalid(CLIP_INFO_VALIDATION))
            {
               this._currBar.updateInfo(this._quantityInClip,this._clipState,this._isReloaded);
            }
            if(isInvalid(CLIP_RELOADING_VALIDATION))
            {
               this._currBar.updateReloadingState(this._reloadingState);
            }
         }
      }
   }
}
