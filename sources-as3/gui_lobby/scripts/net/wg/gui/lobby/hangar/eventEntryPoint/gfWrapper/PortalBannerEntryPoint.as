package net.wg.gui.lobby.hangar.eventEntryPoint.gfWrapper
{
   import flash.display.Sprite;
   import flash.text.TextFormatAlign;
   import net.wg.gui.lobby.hangar.eventEntryPoint.EntryPointSize;
   import net.wg.infrastructure.base.meta.IPortalBannerEntryPointMeta;
   import net.wg.infrastructure.base.meta.impl.PortalBannerEntryPointMeta;
   import net.wg.infrastructure.managers.counter.CounterManager;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   import net.wg.utils.IScheduler;
   
   public class PortalBannerEntryPoint extends PortalBannerEntryPointMeta implements IPortalBannerEntryPointMeta
   {
      
      public static const SIZES:Object = {};
      
      private static const MARGIN:int = 2;
      
      private static const WIDTH_SMALL:int = 160 + MARGIN;
      
      private static const WIDTH_MEDIUM:int = 220 + MARGIN;
      
      private static const WIDTH_BIG:int = 300 + MARGIN;
      
      private static const HEIGHT_SMALL:int = 112 + MARGIN;
      
      private static const HEIGHT_BIG:int = 150 + MARGIN;
      
      private static const INV_COUNTER:String = "InvCounter";
      
      private static const COUNTER_SMALL:CounterProps = new CounterProps(0,0);
      
      private static const COUNTER_BIG:CounterProps = new CounterProps(-2,6,TextFormatAlign.RIGHT,true,CounterProps.DEFAULT_LINKAGE,18);
      
      {
         SIZES[EntryPointSize.EXTRA_SMALL] = [WIDTH_SMALL,HEIGHT_SMALL];
         SIZES[EntryPointSize.EXTRA_SMALL | EntryPointSize.WIDE_MASK] = [WIDTH_BIG,HEIGHT_SMALL];
         SIZES[EntryPointSize.SMALL] = [WIDTH_SMALL,HEIGHT_SMALL];
         SIZES[EntryPointSize.SMALL | EntryPointSize.WIDE_MASK] = [WIDTH_BIG,HEIGHT_SMALL];
         SIZES[EntryPointSize.MEDIUM] = [WIDTH_MEDIUM,HEIGHT_SMALL];
         SIZES[EntryPointSize.MEDIUM | EntryPointSize.WIDE_MASK] = [WIDTH_BIG,HEIGHT_SMALL];
         SIZES[EntryPointSize.BIG] = [WIDTH_BIG,HEIGHT_BIG];
         SIZES[EntryPointSize.BIG | EntryPointSize.WIDE_MASK] = [WIDTH_BIG,HEIGHT_BIG];
      }
      
      private var _counterTarget:Sprite;
      
      private var _counterManager:ICounterManager;
      
      private var _scheduler:IScheduler;
      
      private var _isNew:Boolean;
      
      public function PortalBannerEntryPoint()
      {
         this._counterManager = App.utils.counterManager;
         this._scheduler = App.utils.scheduler;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._counterTarget = new Sprite();
         addChild(this._counterTarget);
      }
      
      override protected function updateSize() : void
      {
         var _loc1_:Array = SIZES[size];
         setSize(_loc1_[0],_loc1_[1]);
         this._counterTarget.x = _loc1_[0];
         invalidate(INV_COUNTER);
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         var _loc2_:CounterProps = null;
         super.draw();
         if(isInvalid(INV_COUNTER))
         {
            this._counterManager.removeCounter(this._counterTarget);
            if(this._isNew)
            {
               if(EntryPointSize.isWide(size) || EntryPointSize.isBig(size))
               {
                  _loc1_ = MENU.COUNTER_NEWCOUNTER;
                  _loc2_ = COUNTER_BIG;
               }
               else
               {
                  _loc1_ = CounterManager.EXCLAMATION_COUNTER_VALUE;
                  _loc2_ = COUNTER_SMALL;
               }
               this._scheduler.scheduleOnNextFrame(this._scheduler.scheduleOnNextFrame,this._counterManager.setCounter,this._counterTarget,_loc1_,null,_loc2_);
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this._counterManager.removeCounter(this._counterTarget);
         this._counterManager = null;
         this._scheduler = null;
         this._counterTarget = null;
         super.onDispose();
      }
      
      public function setIsNew(param1:Boolean) : void
      {
         if(this._isNew != param1)
         {
            this._isNew = param1;
            invalidate(INV_COUNTER);
         }
      }
   }
}
